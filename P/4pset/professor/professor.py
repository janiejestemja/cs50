# Little Professor

from random import randint

def main():
    level = get_level()
    math_problems = []

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y 
        math_problems.append((x, y, solution))

    score = 0

    for x, y, solution in math_problems:
        tries_used = 0

        while tries_used <= 3: 
            if tries_used == 3:
                print(f"{x} + {y} = {solution}")
                break

            answer = int(input(f"{x} + {y} = "))

            if answer == solution:
                score += 1
                break

            else:
                tries_used += 1
                print("EEE")

    print("Score:", score)
        

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in range(1, 4):
                return level
            else:
                pass


def generate_integer(level):
    if level not in range(1, 4):
        raise ValueError("level out of range.")

    match level:
        case 1:
            return randint(1, 9)
        case 2:
            return randint(10, 99)
        case 3:
            return randint(100, 999)


if __name__ == "__main__":
    main()