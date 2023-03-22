import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    # Add a page to the pdf document for each text file
    pdf.add_page()

    # Get the filename without extension
    # and convert to title case
    filename = Path(filepath).stem
    title = filename.split(".")[0].title()

    # Add the name to the pdf
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=12, txt=title, align="L", ln=1)

    # Get the content of each text file
    with open(filepath, "r") as file:
        content = file.read()

    # Add the text file content to the pdf
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
