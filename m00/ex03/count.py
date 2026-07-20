import sys
import string as st

#This function counts the number of upper characters, lower characters,
#punctuation and spaces in a given text.
#c.isupper() counts upper-case letters
#c.islower() counts lower-case letters
#c in string.punctuation counts punctuation
#c == " " counts spaces only
#c.isprintable() counts printable characters
# `s=None` as an arg means that if a user calls `text_analyzer()`, the arg 
# becomes `None`
def text_analyzer(s=None):
    """
    Count printable characters, upper-case letters, lower-case letters,
    punctuation characters, and spaces in a string.
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

#more elegant alternative:
# upper = sum(1 for c in s if c.isupper())
#produces a 1 for each upper char, then sums those ones