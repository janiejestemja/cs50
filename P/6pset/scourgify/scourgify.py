# Scourgify 

import sys
import os
import csv

def main():

    if len(sys.argv) != 3:
        sys.exit("Unexpected amount of commandlinearguments")
    
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("fileendings are not correct.")

    in_csv = os.path.join(os.getcwd(), sys.argv[1])
    if not os.path.exists(in_csv):
        sys.exit("File location not found.")
    
    if not os.path.isfile(in_csv):
        sys.exit("Path does not lead to a file.")

    out_csv = os.path.join(os.getcwd(), sys.argv[2])

    temporary_list = []
    try:
        with open(in_csv) as f:
            reader = csv.DictReader(f)

            for element in reader:
                temporary_list.append(element)

    except FileNotFoundError:
        sys.exit("input file could not be read.")

    final_list = []
    for element in temporary_list:
        last, first = element["name"].split(", ")
        house = element["house"]

        student = {
            "first": first,
            "last": last,
            "house": house
        }
        final_list.append(student)

    with open(out_csv, "w") as f:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for student in final_list:
            writer.writerow(student)

if __name__ == "__main__":
    main()