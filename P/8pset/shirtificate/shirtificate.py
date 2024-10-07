# CS50 Shirtificate

from fpdf import FPDF, XPos, YPos, Align

def main():
    name = input("Name: ").strip()
    make_shirtificate(name)

def make_shirtificate(name):
    shirt_print = name + " took CS50"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", "UI", 36)
    pdf.cell(
        w=200, h=47, text="CS50 Shirtificate", 
        align=Align.C, center=True, 
        new_x=XPos.LEFT, new_y=YPos.NEXT,
        )
    pdf.image(
        "shirtificate.png", w=200, keep_aspect_ratio=True
    )
    pdf.set_x(0)
    pdf.set_y(47)
    pdf.set_font("Helvetica", "", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(
        w=200, h=140, text=shirt_print, 
        align=Align.C, center=True, 
        new_x=XPos.LEFT, new_y=YPos.NEXT,
        )

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
