import json
import ollama
import os
import random
import time


def get_ollama_response(prompt_text, model_name="gpt-oss:120b", max_tokens=150000):
    """
    Makes a call to local Ollama model and returns the response.
    """
    try:
        messages = [{'role': 'user', 'content': prompt_text}]
        response = ollama.chat(
            model=model_name,
            messages=messages,
            options={'num_predict': max_tokens, 'temperature': 0.7}
        )
        return response['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"


def create_user_prompt(training_line):
    """Create user prompt with the specific training line"""

    # Escape the training line for proper JSON formatting in the prompt
    escaped_line = training_line.replace('"', '\\"').replace('\n', '\\n').replace("\\u", '\\\\u')

    user_prompt = f"""I have a training data like follows for my LLM fine tuning,

{escaped_line}

Can you generate ten extra lines from the line to cover a few possibilities of incomplete questions and the corresponding response to ask for more details?

In those ten extra lines, five of them should be a single round of question and answer, and the other five should be multiple rounds of question and answer (at least two rounds of question and answer).

For the single round of question and answer, the question should be an incomplete one and the answer should ask for clarification.

For the multiple rounds of question and answer, the follow-up rounds should be based on the previous rounds, until all the contextually related information is complete so the final anwer, i.e., the database command, can be given.

Please include your response in the jsonl format for those extra lines so I can process your output in a script.

The format should follow this exact structure:
- Start with the same table schema and columns
- Use Q: for questions and A: for answers
- For incomplete questions, the answer should ask for clarification
- Output should be valid JSONL format (one JSON object per line)

In your response, please ensure that all unicode are preserved, i.e., do not convert them to their representative forms."""

    return user_prompt


def process_training_file(input_file, output_file, model_name="gpt-oss:120b", max_tokens=150000):
    """Process each line in the training file and generate multi-turn data"""

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:

        for line_num, line in enumerate(f_in, 1):
            try:
                data = json.loads(line.strip())
                training_line = json.dumps(data)

                print(f"Processing line {line_num}...")

                user_prompt = create_user_prompt(training_line)
                ollama_answer = get_ollama_response(user_prompt, model_name, max_tokens)
                f_out.write(f"# Original line {line_num}:\n")
                f_out.write(f"# {training_line}\n")
                f_out.write("# Generated multi-turn data:\n")
                f_out.write(ollama_answer)
                f_out.write("\n\n")

                # Add a small delay to be gentle on local resources
                time.sleep(0.5)

            except json.JSONDecodeError:
                print(f"Skipping line {line_num}: Invalid JSON")
                continue
            except Exception as e:
                print(f"Error processing line {line_num}: {e}")
                continue


def extract_jsonl_from_output(input_file, output_file):
    """Extract only the JSONL lines from the generated output"""

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            # Check if line looks like JSON (starts with { and ends with })
            if line.startswith('{"text":') and line.endswith('}'):
                try:
                    # Validate it's proper JSON
                    json.loads(line)
                    line = line.replace('\\\\u', '\\u')
                    f_out.write(line + '\n')
                except json.JSONDecodeError:
                    continue


def combine_training_data(original_file, multiturn_file, combined_file):
    """Combine original training data with generated multiturn data"""

    combined_data = []

    # Read original training data
    print(f"Reading original training data from {original_file}...")
    with open(original_file, 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                combined_data.append(data)
            except json.JSONDecodeError:
                continue

    original_count = len(combined_data)
    print(f"Loaded {original_count} original training examples")

    # Read multiturn training data
    print(f"Reading multiturn training data from {multiturn_file}...")
    with open(multiturn_file, 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                combined_data.append(data)
            except json.JSONDecodeError:
                continue

    multiturn_count = len(combined_data) - original_count
    print(f"Loaded {multiturn_count} multiturn training examples")

    # Shuffle the combined data for better training
    random.shuffle(combined_data)

    print(f"Writing combined training data to {combined_file}...")
    with open(combined_file, 'w') as f:
        for data in combined_data:
            f.write(json.dumps(data) + '\n')

    total_count = len(combined_data)
    print(f"Combined training data created with {total_count} total examples:")
    print(f"  - Original: {original_count}")
    print(f"  - Multiturn: {multiturn_count}")
    print(f"  - Total: {total_count}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate multi-turn training data using Ollama")
    parser.add_argument('--model', type=str, default='gpt-oss:120b', help='Ollama model name')
    parser.add_argument('--max-tokens', type=int, default=150000, help='Max tokens for generation')
    parser.add_argument('--input', type=str, default='train.jsonl', help='Input training file')
    parser.add_argument('--output', type=str, default='train_mt.jsonl', help='Output combined file')

    args = parser.parse_args()

    input_file = args.input
    raw_output_file = "multiturn_raw_output.txt"
    multiturn_file = "train_multiturn.jsonl"
    combined_file = args.output

    print(f"Using Ollama model: {args.model}")
    print(f"Max tokens: {args.max_tokens}")
    print(f"Input file: {input_file}")
    print(f"Output file: {combined_file}")

    print("Processing training file...")
    process_training_file(input_file, raw_output_file, args.model, args.max_tokens)

    print("Extracting JSONL data...")
    extract_jsonl_from_output(raw_output_file, multiturn_file)

    print("Combining original and multiturn training data...")
    combine_training_data(input_file, multiturn_file, combined_file)

    print(f"Final combined training data saved to {combined_file}")

    try:
        os.remove(raw_output_file)
        os.remove(multiturn_file)
        print(f"Removed temporary files: {raw_output_file}, {multiturn_file}")
    except OSError as e:
        print(f"Error removing temporary files: {e}")
