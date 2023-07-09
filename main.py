import numpy as np
from matplotlib import pyplot as plt
from reportlab.pdfgen import canvas as cv
from reportlab.lib.pagesizes import letter
from Title_page import *
from Text_Body import draw_body
import json
with open('margins.json') as margins:
    j_margins = margins.read()
j_margins = json.loads(j_margins)
#new doc
cv = SimpleDocTemplate(
            "out/out.pdf",
            pagesize=letter,
            rightMargin=j_margins["portrait"]["right"]*cm, leftMargin=j_margins["portrait"]["left"]*cm,
            topMargin=j_margins["portrait"]["up"]*cm, bottomMargin=j_margins["portrait"]["down"]*cm,
            )
#generate font styles
styles = UdeS_style_sheet()
# add firstpage
firstpage = draw_titlepage(styles)
body = draw_body(styles)
doc = firstpage + body
cv.build(doc)

