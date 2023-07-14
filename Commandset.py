#TODO think of a command set user can use to add features
#Figure : "figure":["filename", "figname", X(mm),Y(mm)] // no x and y will be default
#Callbacks/matplotlib "callback": ["methodname", "jason_subcommand"] // jason_subcommand how to process returned data like figure or table etc
#Tables: "table":"filename" // use panda and open file
#Equations //TBD
#Citations "Quote":"jason item reference"
#Import .txt(from line to line or all file) and img
#page break
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak
from reportlab.lib.units import cm
import json
import os
import urllib3
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from dataclasses import dataclass
import requests
@dataclass
class figure:
    name: str
    number: int
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

@dataclass
class table_of_figure:
    table: list[figure]
    lastfignumber : int = 0


figures_tab = table_of_figure([])
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
    if (keys.startswith("figure")):
        return printfig(values, styles)
    return flowables
    # TODO add more command to the list


def printfig(values, styles):
    global figures_tab
    flowables = []
        #""" Get a python logo image for this example """
    if not os.path.exists("Body_text/"+values[0]):
        img_data = requests.get(values[0]).content
        filename, file_extension = os.path.splitext(values[0])
        with open("Body_text/temp_img"+ file_extension, 'wb') as handler:
            values[0] = "temp_img"+ file_extension
            handler.write(img_data)
    #add figure
    figures_tab.lastfignumber = figures_tab.lastfignumber + 1
    figures_tab.table.append(figure(values[1],figures_tab.lastfignumber))
    flowables.append(Image("Body_text/" + values[0],width=values[2],height=values[3],kind='direct',mask="auto", lazy=1, hAlign='CENTER', useDPI=False))#TODO add fig size
    #add figname
    para = Paragraph("Figure"+str(figures_tab.table[-1].number) +" : "+ figures_tab.table[-1].name, style=styles["Definition"])
    flowables.append(para)
    return flowables