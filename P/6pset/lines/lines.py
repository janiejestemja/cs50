# Lines of Code

import os
import sys

def main():
    if len(sys.argv) != 2: 
        sys.exit("Unexpected amount of commandlinearguments.")
    
    # checking supposed filelocation
    sup_f_loc = os.path.join(os.getcwd(), sys.argv[1])
    if not os.path.exists(sup_f_loc):
        sys.exit("File location not found.")
    
    if not os.path.isfile(sup_f_loc):
        sys.exit("Path does not lead to a file.")

    try:   
        with open(sup_f_loc) as f:
            reader = f.readlines()
    except FileNotFoundError:
        sys.exit("File not found.")
    else:
        count = 0
        for line in reader:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            else:
                count += 1
        print(count)

if __name__ == "__main__":
    main()