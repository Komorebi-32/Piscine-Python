"""Reverse and swap case of the command-line input string.

This script concatenates all command-line arguments (after the script name)
into a single string separated by spaces, reverses the resulting string,
and swaps the case of each character, then prints the transformed string.

Usage:
    python3 exec.py Hello world

Example:
    Input:  Hello world
    Output: DLROw OLLEh
"""

import sys

if len(sys.argv) < 2:
    print("Usage: python3 exec.py <string>")
    sys.exit(1)

text = sys.argv[1]

if len(sys.argv) > 2:
    i = 2
    while i < len(sys.argv):
        text += " "
        text += sys.argv[i]
        i += 1

result = text[::-1].swapcase()
print(result)
