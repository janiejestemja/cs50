# Adieu, Adieu

from inflect import engine 

def main():
    p = engine()
    names = []

    while True:
        try:
            name = input("Name: ")

        except EOFError:
            formatted_names = p.join(names, final_sep="")

            print("")
            print("Adieu, adieu, to", formatted_names)
            break

        else:
            names.append(name)


if __name__ == "__main__":
    main()