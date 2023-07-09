from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak
from reportlab.lib.units import cm
import json
import os
from Commandset import compute_command
def draw_body(styles):
    flowables = []
    for filename in os.listdir("Body_text/"):
       if filename.endswith('.json'):
           with open(os.path.join("Body_text/", filename), 'r') as f: # open in readonly mode
              j_text = f.read()
              j_text = json.loads(j_text)
              flowables = flowables + process_jason(styles, j_text)
    return  flowables
def process_jason(styles, jason):
    flowables = []
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_paragraph(styles,values,keys)
    return flowables


def process_paragraph(styles, jason, title):
    flowables = []
    para = Paragraph(title, style=styles["Heading1"])
    flowables.append(para)
    for keys,values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_paragraph(styles,values,keys)
            pass
        flowables = flowables + compute_command(keys,values, styles)
        # if(keys.startswith("text")):
        #     para = Paragraph(values, style=styles["Normal"])
        #     flowables.append(para)
        #     pass
        # if (keys.startswith("file")):
        #     if type(values) is str:
        #         try :
        #             f = open( "Body_text/"+ values, "r")
        #             para = Paragraph(f.read(), style=styles["Normal"])
        #             flowables.append(para)
        #         except:
        #             print(("error parsing file: no file , skipping"))
        #             pass
        #     else:
        #         print("error parsing file: not a string")
        #     pass
        # #TODO add more command to the list

    return flowables

def process_sub_paragraph(styles, jason,subtitle):
    flowables = []
    para = Paragraph("\t"+subtitle, style=styles["Heading2"])
    flowables.append(para)
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_sub_paragraph(styles,values, keys)
            pass
        flowables = flowables + compute_command(keys, values, styles)
    return flowables
def process_sub_sub_paragraph(styles, jason, subsubtitle):
    flowables = []
    para = Paragraph("\t" + subsubtitle, style=styles["Heading3"])
    flowables.append(para)
    for keys, values in jason.items():
        if type(values) is dict:
            flowables = flowables + process_sub_sub_paragraph(styles, values, keys)
            pass
        flowables = flowables + compute_command(keys, values, styles)
    return flowables