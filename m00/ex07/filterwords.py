import sys
import string as st

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit(1)

try:
    n = int(sys.argv[2])
    word_list = [''.join(char for char in word if char not in st.punctuation) for word in sys.argv[1].split()]
    print_list = [word for word in word_list if len(word) > n]
    print(print_list)
except ValueError:
    print("CRITICAL ERROR 404 BLUE SCREEN OF DEATH BYYYYYYYEEEEEEEE")
    sys.exit(1)
