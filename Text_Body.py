from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak
from reportlab.lib.units import cm
import json
import os
from Commandset import compute_command
from dataclasses import dataclass

@dataclass
class titlenumbering:
    titles: int = 1
    subtitles: int = 1
    subsubtitle: int = 1

def draw_body(styles):
    flowables = []
    titlenumber = titlenumbering()
    for filename in os.listdir("Body_text/"):
       if filename.endswith('.json'):
           with open(os.path.join("Body_text/", filename), 'r') as f: # open in readonly mode
              j_text = f.read()
              j_text = json.loads(j_text)
              flowables = flowables + process_jason(styles, j_text,titlenumber)
    return  flowables
def process_jason(styles, jason,number):
    flowables = []
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_paragraph(styles,values,keys,number)
    return flowables


def process_paragraph(styles, jason, title,number):
    flowables = []
    para = Paragraph(str(number.titles)+". "+title, style=styles["Heading1"])
    number.titles = number.titles + 1
    flowables.append(para)
    for keys,values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_paragraph(styles,values,keys,number)
            pass
        flowables = flowables + compute_command(keys,values, styles)
    return flowables
def process_sub_paragraph(styles, jason,subtitle,number):
    flowables = []
    para = Paragraph("\t"+str(number.titles)+"."+str(number.subtitles)+". "+subtitle, style=styles["Heading2"])
    number.subtitles =number.subtitles + 1
    flowables.append(para)
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_sub_paragraph(styles,values,  keys,number)
            pass
        flowables = flowables + compute_command(keys, values, styles)
    return flowables
def process_sub_sub_paragraph(styles, jason, subsubtitle,number):
    flowables = []
    para = Paragraph("\t\t" +str(number.titles)+"."+str(number.subtitles)+"."+str(number.subsubtitle)+". "+subsubtitle, style=styles["Heading3"])
    flowables.append(para)
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_sub_paragraph(styles, values, keys,number)
            pass
        flowables = flowables + compute_command(keys, values, styles)
    return flowables