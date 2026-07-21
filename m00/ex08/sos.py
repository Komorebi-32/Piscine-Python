import sys

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/",
}


def main():
    if len(sys.argv) < 2:
        print("usage: python3 sos.py <message>")
        return
    
    message = " ".join(sys.argv[1:]).upper()

    if any(ch not in MORSE for ch in message):
        print("ERROR")
        sys.exit(1)

    print(" ".join(MORSE[ch] for ch in message))


if __name__ == "__main__":
    main()
