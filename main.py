from cli_agent import ask_llm
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Smart CLI agent")
    parser.add_argument("question", nargs="?", help="Ask question")

    args = parser.parse_args()

    if args.question is None:
        print("\033[1m M'embête pas si tu n'as pas de question à poser… 😴💤\033[0m")
    else:
    	answer = ask_llm(args.question)
    	print(answer)

if __name__ == "__main__":
    main()