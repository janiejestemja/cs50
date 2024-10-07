# NUMB3RS

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try: 
        elements = list(ip.split("."))

    except (ValueError, TypeError):
        return False

    else: 
        try:
            numb3rs = list()

            for element in elements:
                numb3rs.append(int(element))

        except ValueError:
            return False 

        else:
            if len(numb3rs) == 4:

                for numb3r in numb3rs:
                    if numb3r > 255:
                        return False

                    elif numb3r < 0:
                        return False

                    else:
                        return True
            else:
                return False


if __name__ == "__main__":
    main()