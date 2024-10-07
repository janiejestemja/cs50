# Guessing Game

from random import randint

def main():
    while True:

        try:
            level = int(input("Level: "))

        except ValueError:
            pass

        else:
            solution = randint(1, level)
            break

    while True:

        try:
            guess = int(input("Guess: "))
        
        except ValueError:
            pass
        
        else:
            if guess > solution:
                print("Too small!")

            elif guess < solution:
                print("Too large!")

            else:
                print("Just right!")
                break

if __name__ == "__main__":
    main()