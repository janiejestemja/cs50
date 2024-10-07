# Response Validation 
from validator_collection import checkers

def main():
    if checkers.is_email(input("Email: ").strip()):
        print("Valid")
    else:
        print("Invaild")

if __name__ == "__main__":
    main()