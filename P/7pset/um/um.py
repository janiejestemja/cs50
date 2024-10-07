# Regular, um, Expressions

import re

def main():
    print(count(input("Text: ")))

def count(s):
    string = s.lower()
    if matches := re.findall(r"(\bum\b)", string, re.IGNORECASE):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()