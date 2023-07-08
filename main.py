import numpy as np
from matplotlib import pyplot as plt
from reportlab.pdfgen import canvas as cv
from reportlab.lib.pagesizes import letter
from Title_page import *
import json
with open('margins.json') as margins:
    j_margins = margins.read()
j_margins = json.loads(j_margins)
#new doc
cv = SimpleDocTemplate(
            "titlepage.pdf",
            pagesize=letter,
            rightMargin=j_margins["portrait"]["right"]*cm, leftMargin=j_margins["portrait"]["left"]*cm,
            topMargin=j_margins["portrait"]["up"]*cm, bottomMargin=j_margins["portrait"]["down"]*cm,
            )
# add firstpage
firstpage = draw_titlepage()

doc = firstpage
cv.build(doc)

