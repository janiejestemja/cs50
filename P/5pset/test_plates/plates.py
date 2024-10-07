# Vanity Plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # lengthcheck
    if not len(s) in range(2, 7) or not s.isalnum():
        return False

    # first two letters check
    if not s[0:2].isalpha():
        return False

    # numbers check
    for i in range(1, len(s)):
        # check if character is a number
        if s[i - 1].isnumeric() and s[i].isalpha():
            return False

    # check if first number is zero
    for i in range(1, len(s)):
        if s[i - 1].isalpha() and s[i] == "0":
            return False

    # because all checks went through just return true
    return True


if __name__ == "__main__":
	main()