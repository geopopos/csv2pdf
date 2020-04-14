import os
import csv
import textwrap
from fpdf import FPDF

def csv2pdf(data):
    pdf = FPDF()
    
    with open(data, newline='') as csvfile:
        leads = csv.reader(csvfile, delimiter=',')
        headers = next(leads)
        for row in leads:
            pdf.add_page()
            for column in zip(headers, row):
                pdf.set_font("Arial", size=18)
                header = column[0].encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(200, 10, txt=header, ln=1, align="L")
                pdf.set_font("Arial", size=12)
                values = column[1].encode('latin-1', 'replace').decode('latin-1')
                values = textwrap.wrap(values, width=99)
                for value in values:
                    pdf.cell(200, 10, txt=value, ln=1, align="L")
    
    pdf.output("leads.pdf")

data = os.environ["SHEET_NAME"]
csv2pdf(data)
