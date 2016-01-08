import sys
import string

def letter_count(text, letters = string.ascii_letters):
    letters = frozenset(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ("-h", "--help"):
        print("Usage: {0} letter".format(sys.argv[0]))
        sys.exit()
    else:
        print(letter_count(sys.argv[1], ))

main()
