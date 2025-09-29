#!/usr/bin/env python3
"""Part 1 starter CLI (Complete the two TODOs in the code below)."""
from .constants import BANNER, HELP
from .sonnet import SONNET

def manual_count_occurrences(text: str, pattern: str) -> int:
    """TODO: implement naive manual scan counting overlapping occurrences.
    Requirements:
    - case-insensitive (e.g., caller will lowercase inputs)
    - no str.find, no 'in' for text search, no regex
    """
    # Starter: a placeholder returning 0 so tests fail until implemented.
    if not text or not pattern:
        return 0
    # >>> replace the following with a real manual scan <<<
    text_count = 0
    for i in range(len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)] == pattern):
            text_count += 1
    return text_count


def print_result(query: str, total: int, title_count: int, line_count: int) -> None:
    print(f"Matches for \"{query}\": {total} (title: {title_count}, lines: {line_count})")

def main() -> None:
    print(BANNER)
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break
        if not raw:
            continue
        if raw.startswith(":"):
            if raw == ":quit":
                print("Bye.")
                break
            if raw == ":help":
                print(HELP)
                continue
            print("Unknown command. Type :help for commands.")
            continue

        # TODO: Search the SONNET title and the SONNET lines for the query given by the user.
        #  Do this in an case-insensitive way
        #  title_count reflects the number of occurrences in the title of the sonnet, and line_count those in the lines
        #  of the sonnet.
        #  Call your implementation of the function manual_count_occurrences to get the counts in the title and the
        #  lines of the sonnet.

        title, lines = SONNET["title"], SONNET["lines"]
        title_count = manual_count_occurrences(title.lower(), raw.lower())
        line_count = 0
        for line in lines:
            current_line_count = manual_count_occurrences(line.lower(), raw.lower())
            line_count += current_line_count
        total = title_count + line_count
        print_result(raw, total, title_count, line_count)

if __name__ == "__main__":
    main()
