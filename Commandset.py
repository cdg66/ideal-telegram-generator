#TODO think of a command set user can use to add features
#Figure
#Callbacks/matplotlib
#Tables
#Equations
#Citations
#Import .txt and img
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak
from reportlab.lib.units import cm
import json
import os
def compute_command(keys,values, styles):
    flowables = []
    if (keys.startswith("text")):
        para = Paragraph(values, style=styles["Normal"])
        flowables.append(para)
        return flowables
    if (keys.startswith("file")):
        if type(values) is str:
            try:
                f = open("Body_text/" + values, "r")
                para = Paragraph(f.read(), style=styles["Normal"])
                flowables.append(para)

            except:
                print(("error parsing file: no file , skipping"))
            return flowables
        else:
            print("error parsing file: not a string")
            return flowables
    return flowables
    # TODO add more command to the list