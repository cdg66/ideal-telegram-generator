#TODO think of a command set user can use to add features
#Figure : "figure":["filename", "figname", X(mm),Y(mm)] // no x and y will be default // done
#Callbacks/matplotlib "callback": ["methodname", "jason_subcommand"] // jason_subcommand how to process returned data like figure or table etc
#Tables: "table":["filename", "tabname"] // use panda and open file
#Equations //TBD
#Citations "Quote":"jason item reference"
#file: .txt(from line to line or all file)  //done
#text: add inline text directly in the json file
#page break
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer , PageBreak, Table, TableStyle
from reportlab.lib import colors
import os
from reportlab.platypus import Image
from dataclasses import dataclass
import requests
import pandas as pd
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
@dataclass
class table_of_tabs:
    table: list[figure]
    lastfignumber : int = 0
tab_of_tabs = table_of_tabs([])

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
    if (keys.startswith("table")):
        return printtabs(values, styles)
    return flowables
    # TODO add more command to the list


def printfig(values, styles):
    global figures_tab
    flowables = []
        #""" Get a python logo image for this example """
    if not os.path.exists("Body_img/"+values[0]):
        img_data = requests.get(values[0]).content
        filename, file_extension = os.path.splitext(values[0])
        with open("Body_img/temp_img"+ file_extension, 'wb') as handler:
            values[0] = "temp_img"+ file_extension
            handler.write(img_data)
    #add figure
    figures_tab.lastfignumber = figures_tab.lastfignumber + 1
    figures_tab.table.append(figure(values[1],figures_tab.lastfignumber))
    flowables.append(Image("Body_img/" + values[0],width=values[2],height=values[3],kind='direct',mask="auto", lazy=1, hAlign='CENTER', useDPI=False))
    #add figname
    para = Paragraph("Figure "+str(figures_tab.table[-1].number) +" : "+ figures_tab.table[-1].name, style=styles["Definition"])
    flowables.append(para)
    return flowables
def readcsv(file):
    return pd.read_csv("Body_table/"+file)
def readjson(file):
    return pd.read_json("Body_table/"+file, orient='split')
def readXcel(file):
    return pd.read_excel("Body_table/"+file, index_col=0)
openarray = {
    "csv": readcsv,
    "json": readjson,
    "xls": readXcel,
    "xlsx": readXcel
}
def printtabs(values, styles):
    global table_of_tabs
    global openarray
    flowables = []
    #append tab name
    tab_of_tabs.lastfignumber = tab_of_tabs.lastfignumber + 1
    tab_of_tabs.table.append(figure(values[1], tab_of_tabs.lastfignumber))
    para = Paragraph("Tableau " + str(tab_of_tabs.table[-1].number) + " : " + tab_of_tabs.table[-1].name,
                     style=styles["Definition"])
    flowables.append(para)
    #open tabs with pandas
    filetype = values[0].split(".")
    dataframe = openarray[filetype[-1]](values[0])
    #append tab
    table = list(dataframe.columns.values)
    #table.append()
    t = Table([table]+dataframe.values.tolist())
    t.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,0),1,colors.black),
                           ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
                           ('LINEABOVE', (0, 1), (-1, 1), 1, colors.black),
                           ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
                           ]))
    flowables.append(t)
    return flowables


