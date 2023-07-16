
from reportlab.lib.units import mm
body_page_num = 1
def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    global body_page_num
    #page_num = canvas.getPageNumber()
    text = "%s" % body_page_num
    body_page_num = body_page_num + 1
    canvas.drawRightString(200*mm, 20*mm, text)