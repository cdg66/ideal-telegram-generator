from reportlab.lib.styles import getSampleStyleSheet

def UdeS_style_sheet():
    styles = getSampleStyleSheet()
    styles["Normal"].alignment = 4
    #TODO modfy stylesheet to match the one of the university
    return styles