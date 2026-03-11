#!/usr/bin/env python3
"""Interactive CLI to ask questions about the TechStore database."""

from dotenv import load_dotenv

load_dotenv()

from app.agent import ask_dataframes  # noqa: E402


def main():
    print("TechStore DB Assistant (type 'exit' to quit)")
    print("=" * 50)
    while True:
        try:
            question = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question or question.lower() in ("exit", "quit"):
            break
        try:
            answer = ask_dataframes(question)
            print(f"\n{answer}")
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
