import json
from openai import OpenAI
import os
import random

with open(".openai_apikey", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)


def get_gpt4o_response(prompt_text):
    """
    Makes an API call to OpenAI's GPT-4o model and returns the response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating training data."},
                {"role": "user", "content": prompt_text}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


def create_user_prompt(training_line):
    """Create user prompt with the specific training line"""

    # Escape the training line for proper JSON formatting in the prompt
    escaped_line = training_line.replace('"', '\\"').replace('\n', '\\n').replace("\\u", '\\\\u')

    user_prompt = f"""I have a training data like follows for my LLM fine tuning,

{escaped_line}

Can you generate five extra lines from the line to cover a few possibilities of incomplete questions and the corresponding response to ask for more details? Please include your response in the jsonl format for those extra lines so I can process your output in a script.

The format should follow this exact structure:
- Start with the same table schema and columns
- Use Q: for questions and A: for answers
- For incomplete questions, the answer should ask for clarification
- Output should be valid JSONL format (one JSON object per line)

In your response, please ensure that all unicode are preserved, i.e., do not convert them to their representative forms."""

    return user_prompt


def process_training_file(input_file, output_file):
    """Process each line in the training file and generate multi-turn data"""

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:

        for line_num, line in enumerate(f_in, 1):
            try:
                data = json.loads(line.strip())
                training_line = json.dumps(data)

                print(f"Processing line {line_num}...")

                user_prompt = create_user_prompt(training_line)
                gpt4o_answer = get_gpt4o_response(user_prompt)
                f_out.write(f"# Original line {line_num}:\n")
                f_out.write(f"# {training_line}\n")
                f_out.write("# Generated multi-turn data:\n")
                f_out.write(gpt4o_answer)
                f_out.write("\n\n")

                # Add a small delay to avoid rate limiting
                import time
                time.sleep(1)

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
    input_file = "train_test.jsonl"
    raw_output_file = "multiturn_raw_output.txt"
    multiturn_file = "train_multiturn.jsonl"
    combined_file = "train_mt.jsonl"

    print("Processing training file...")
    process_training_file(input_file, raw_output_file)

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
