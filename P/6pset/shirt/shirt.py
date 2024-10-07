# CS50 P-Shirt

import os
import sys
from PIL import Image, ImageOps

def main():

    if len(sys.argv) != 3:
        sys.exit("Unexpected amount of command line arguments(expecting 2)")

    accepted_extensions = [".jpg", ".jpeg", ".png"]

    im_extension = ""
    for extension in accepted_extensions:
        if sys.argv[1].endswith(extension) and sys.argv[2].endswith(extension):
            im_extension = im_extension + extension

    if im_extension == "":
        sys.exit("Input and Output have different extensions.")


    # checking supposed filelocation
    source_image = os.path.join(os.getcwd(), sys.argv[1])
    if not os.path.exists(source_image):
        sys.exit("File location not found.")
    
    if not os.path.isfile(source_image):
        sys.exit("Path does not lead to a file.")

    output_image = os.path.join(os.getcwd(), sys.argv[2])
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    p_shirt_loc = os.path.join(dir_path, "shirt.png")
    
    if not os.path.exists(p_shirt_loc):
        sys.exit("Sorry, out of P-Shirts (file 'shirt.png' not found by os).")

    try:
        with Image.open(source_image) as im:
            imported_im = im.convert("RGBA")

    except OSError:
        sys.exit("Trouble opening the inputted image.")

    try: 
        with Image.open(p_shirt_loc) as im:
            shirt = im.convert("RGBA")

    except FileNotFoundError:
        sys.exit("Sorry, out of P-Shirts (file 'shirt.png' not found by Pil).")

    imported_im = ImageOps.fit(imported_im,(shirt.size))
    imported_im.paste(shirt, shirt)

    im = imported_im.convert("RGB")
    im.save(output_image)
    
    shirt.close()


if __name__ == "__main__":
    main()