import ollama
import argparse


def main():
    parser = argparse.ArgumentParser(description="Ollama prompt runner")
    parser.add_argument('--model', type=str, default='mistral_pd', help='Model name')
    parser.add_argument('--max-tokens', type=int, default=50, help='Max tokens')
    parser.add_argument('--prompt', type=str, required=True, help='Prompt to send')
    args = parser.parse_args()

    messages = [{'role': 'user', 'content': args.prompt}]
    response = ollama.chat(
        model=args.model,
        messages=messages,
        options={'num_predict': args.max_tokens}
    )
    print(response['message']['content'])


if __name__ == "__main__":
    main()
