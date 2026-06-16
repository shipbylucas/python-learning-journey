from fpdf import FPDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
import re

def main():
    global name
    name = get_name()
    shirt(name)
    pdf.output("shirtificate.pdf")

def get_name():
    while True:
        name = input("Name: ").strip().title()
        if re.search(r"^([A-Z]*[a-z]*(\s)?)+$", name):
            return name
        else:
            raise ValueError("Invalid name")

def shirt(name):
    pdf.add_page()

    pdf.set_xy(41.9, 27.5)
    pdf.set_font("Helvetica", style="", size=48)
    pdf.cell(128.7, 20.2, txt="CS50 Shirtificate", align="C", border=0, ln=False, fill=False)

    pdf.image("shirtificate.png", x=10.5, y=70, w=190)

    pdf.set_xy(58.6, 130.4)
    pdf.set_font("Helvetica", style="", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(94.6, 10, txt=name + " took CS50", align="C", border=0, ln=False, fill=False)

if __name__ == "__main__":
    main()
