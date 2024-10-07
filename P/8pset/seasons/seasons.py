# Seasons of Love

import sys
import re
from inflect import engine
from datetime import date 


def main():
    s = input("Date: ").strip()
    date_today = date.today()

    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):

        try:
            a_date = date(
            year = int(match.group(1)), 
            month = int(match.group(2)), 
            day = int(match.group(3)), 
            )

        except ValueError:
            sys.exit("Invalid input")

        else:
            try:
                _ = func(date_today, a_date)
            except ValueError:
                sys.exit("Invalid input.")
            else:
                print(func(date_today, a_date))
    else:
        sys.exit("Invalid input.")


def func(date_today, a_date):
    # input validation
    teda = date(year=1, month=1, day=1)
    if type(date_today) != type(teda) or type(a_date) != type(teda):
        raise ValueError("func only accepts arguments of type datetime.date")
    p = engine()
    delta = date_today - a_date 
    if delta.days < 0:
        raise ValueError("given date is in the future.")
    return p.number_to_words(delta.days * 24 * 60, andword="") + " minutes."


if __name__ == "__main__":
    main()