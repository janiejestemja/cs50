# Working 9 to 5

import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # checking and assigning
    if match := re.search(r"^(1?\d)(?::([0-5]\d))? ([A|P])M to (1?\d)(?::([0-5]\d))? ([A|P])M$", s, re.IGNORECASE):
        sth = int(match.group(1))
        stap = match.group(3).lower()
        enh = int(match.group(4))
        enap = match.group(6).lower()
        print(enap)
        # doing leftover checks 
        if sth > 12 or enh > 12:
            raise ValueError
        # setting up the start 
        if sth < 12 and stap == "p":
            sth = sth + 12

        if sth == 12 and stap == "a":
            sth = 0

        if stm := match.group(2):
            start = f"{sth:02}:{stm:02}"
        else:
            start = f"{sth:02}:00"

        # setting up the end
        if enh < 12 and enap == "p":
            enh = enh + 12

        if enh == 12 and enap == "a":
            enh = 0

        if enm := match.group(5):
            end = f"{enh:02}:{enm:02}"
        else:
            end = f"{enh:02}:00"

        # returning result
        return str(start + " to " + end)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
