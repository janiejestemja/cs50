# Bitcoin Price Index

import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("No command line argument provided(expecting a floating point number).")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Unexpected command line argument provided(expecting a floating point number).")
    else: 
        try: 
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.exceptions.RequestException:
            sys.exit("Something went wrong while getting the request.")
        else: 
            try: 
                r = r.json()
            except requests.exceptions.JSONDecodeError:
                sys.exit("Decoding of the response failed.")
            else:
                rate_float = r["bpi"]["USD"]["rate_float"]
                print(f"${rate_float * float(sys.argv[1]):,.4f}")


if __name__ == "__main__":
    main()