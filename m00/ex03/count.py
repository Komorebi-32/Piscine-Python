"""Simple text analysis utilities used in exercises.

This module provides text_analyzer(), a small utility that counts printable
characters, upper-case letters, lower-case letters, punctuation characters,
and spaces in a provided string or user input.
"""

import sys
import string as st


def text_analyzer(s=None):
    """Analyze a text and print counts for several character categories.

    The function concatenates and analyzes the provided string `s`. If `s` is
    None or an empty string, the user is prompted to enter the text interactively.
    The function prints the number of printable characters, upper-case letters,
    lower-case letters, punctuation characters, and spaces to stdout.

    Args:
        s (str | None): Text to analyze. If None or '', the user is prompted.
            The function accepts any Python string.

    Raises:
        TypeError: If the provided argument is not a string.

    Examples:
        >>> text_analyzer("Hello, World!")
        The text contains 13 printable characters.
        2 upper-case characters.
        8 lower-case characters.
        2 punctuation characters.
        1 spaces.
    """
    try:
        if s is None or s == "":
            s = input("What is the text to analyze?\n")
        printable = 0
        upper = 0
        lower = 0
        punctuation = 0
        spaces = 0
        for c in s:
            if c.isprintable():
                printable += 1
            if c.isupper():
                upper += 1
            if c.islower():
                lower += 1
            if c in st.punctuation:
                punctuation += 1
            if c == " ":
                spaces += 1

        print(f"The text contains {printable} printable characters.")
        print(f"{upper} upper-case characters.")
        print(f"{lower} lower-case characters.")
        print(f"{punctuation} punctuation characters.")
        print(f"{spaces} spaces.")
    except TypeError:
        print("Error: argument is not a string")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        text_analyzer()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("Error: Too many arguments")
        sys.exit(1)
