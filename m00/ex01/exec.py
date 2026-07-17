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