import sys

if len(sys.argv) < 2:
    print("Usage: python3 whois.py <number>")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Error: Too many arguments")
    sys.exit(1)

# The classical Python mentality is that it's easier to ask forgiveness than permission. 
# In other words, don't check whether x is an integer; assume that it is and catch
# the exception results if it isn't
try:
    n = int(sys.argv[1])
    if n == 0:
        print("I'm Zerooooo")
        sys.exit(0)
    elif n % 2 == 0:
        print("I'm Even")
        sys.exit(0)
    else:
        print("I'm Odd")
        sys.exit(0)
except ValueError:
    print("Error: argument is not an integer")
    sys.exit(1)