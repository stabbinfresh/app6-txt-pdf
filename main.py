import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    title = filename.split(".")[0].title()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=12, txt=title, align="L", ln=1)

pdf.output("output.pdf")
