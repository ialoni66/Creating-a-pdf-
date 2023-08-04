from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


animals = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for file in animals:
    pdf.add_page()
    animal = Path(file).stem
    animal = animal.title()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=24, txt=f"{animal}", ln=1)
    with open(file, 'r') as text:
        content = text.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=6, txt=f"{content}")
pdf.output("output.pdf")




