import numpy as np
from matplotlib import pyplot as plt
from reportlab.pdfgen import canvas as cv
from reportlab.lib.pagesizes import letter
from Title_page import *
from Text_Body import draw_body
import json
from reportlab.lib.units import mm
from pagination import addPageNumber



if __name__ == '__main__':
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
    #compute body
    body = draw_body(styles)
    #compute toc

    #compute tof

    #compute tot

    #compute anexes

    #mergre everything
    doc = firstpage + body
    #generate document
    cv.build(doc,onLaterPages=addPageNumber)

