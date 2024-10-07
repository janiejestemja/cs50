# Pizza Py

import os
import sys 
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) != 2: 
        sys.exit("Unexpected amount of commandlinearguments.")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Unexpected fileending.")

    # checking supposed filelocation
    sup_f_loc = os.path.join(os.getcwd(), sys.argv[1])
    if not os.path.exists(sup_f_loc):
        sys.exit("File location not found.")
    
    if not os.path.isfile(sup_f_loc):
        sys.exit("Path does not lead to a file.")

    try: 
        with open(sup_f_loc) as f:
            reader = csv.DictReader(f)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found.")

if __name__ == "__main__":
    main()