from UdeS_StyleSheet import UdeS_style_sheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak
from reportlab.lib.units import cm
import json
def draw_titlepage():
    with open('titlepage.json') as titlepage:
        j_text = titlepage.read()
    j_text = json.loads(j_text)

    print (j_text)

    styles = UdeS_style_sheet()
    headderstyle = styles['Normal']
    headderstyle.alignment = 1
    flowables = []
    for i in j_text["Headder"]:
        para = Paragraph(i, style=headderstyle)
        flowables.append(para)
    flowables.append(Spacer(1, 5 * cm))
    para = Paragraph(j_text["Title"]+"\r\n", style=styles["Title"])
    flowables.append(para)
    flowables.append(Spacer(1, 4 * cm))
    para = Paragraph(j_text["Sub_Titile"], style=headderstyle)
    flowables.append(para)
    #flowables.append(Spacer(1, 1 * cm))
    para = Paragraph(j_text["Classnumber"], style=headderstyle)
    flowables.append(para)
    flowables.append(Spacer(1, 2 * cm)) #TODO make spcaer automatic
    for j in j_text["Teacher"]:
        para = Paragraph(j, style=headderstyle)
        flowables.append(para)
    flowables.append(Spacer(1, 2 * cm))
    for k in j_text["Team"]["Team_number"]:
        para = Paragraph(k, style=headderstyle)
        flowables.append(para)
    for l in j_text["Team"]["Teammate"]:
        para = Paragraph(l["name"]+l["separator"]+l["cip"]+l["separator"], style=headderstyle)
        flowables.append(para)
    flowables.append(Spacer(1, 2.5 * cm))
    para = Paragraph(j_text["location"]+j_text["date"], style=headderstyle)
    flowables.append(para)
    flowables.append(PageBreak())
    return flowables

