# Watch on YouTube

import re

def main():
    print(parse(input("HTML: ").strip()))

def parse(s):
    # applying re.search per its documentation
    if matches := re.search( 
        r"<iframe .*src=(?:'|\")https?://(?:www\.)?youtube\.com/embed/(.*)(?:'|\").*></iframe>", 
        s, re.IGNORECASE
        ):
        # returning reformatted url
        return "https://youtu.be/" + matches.group(1)

if __name__ == "__main__":
    main()