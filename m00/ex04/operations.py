import sys

LABEL_WIDTH = 12


def print_aligned(label, value):
    print(f"{label:<{LABEL_WIDTH}}{value}")


if len(sys.argv) == 1:
    print("Usage: python3 operations.py <number1> <number2>")
    sys.exit(1)

if len(sys.argv) != 3:
    print("Incorrect number of arguments")
    sys.exit(1)

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    total = n1 + n2
    print_aligned("Sum:", total)
    diff = n1 - n2
    print_aligned("Difference:", diff)
    prod = n1 * n2
    print_aligned("Product:", prod)
    try:
        quotient = n1 / n2
        print_aligned("Quotient:", quotient)
        remainder = n1 % n2
        print_aligned("Remainder:", remainder)
    except ZeroDivisionError:
        print_aligned("Quotient:", "ERROR (division by zero)")
        print_aligned("Remainder:", "ERROR (modulo by zero)")
except ValueError:
    print("Only integers accepted")
    sys.exit(1)
