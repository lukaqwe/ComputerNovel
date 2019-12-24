import jinja2
import pdfkit

from dice import *
from colors import *

WE = False


def empath():
    global WE, isHe

    if isHe:
        result = ['I vs He', '', '', '', '', '', '', '']
        tmp = I_HeShe()
        result[1] = tmp[0]

        if tmp[1]:
            tmp = IorHeShe_IandHeShe()
            result[2] = 'I or He vs I and He'
            result[3] = tmp[0]
            if tmp[1]:
                tmp = You_IorHeShe()
                result[4] = 'You vs I or He'
                result[5] = tmp[0]
                if tmp[1]:
                    result[6] = 'We'
                    result[7] = we()
                    WE = True
    else:  # do the exact same thing for a she
        result = ['I vs She', '', '', '', '', '', '', '']
        tmp = I_HeShe()
        result[1] = tmp[0]

        if tmp[1]:
            tmp = IorHeShe_IandHeShe()
            result[2] = 'I or She vs I and She'
            result[3] = tmp[0]
            if tmp[1]:
                tmp = You_IorHeShe()
                result[4] = 'You vs I or She'
                result[5] = tmp[0]
                if tmp[1]:
                    result[6] = 'We'
                    result[7] = we()
                    WE = True
    return result


def render_empath():
    emPATH = empath()

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/empath.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(
        I_HeShe=emPATH[0], I_HeShe_text=emPATH[1], IorHeShe_IandHeShe=emPATH[2],
        IorHeShe_IandHeShe_text=emPATH[3], You_IorHeShe=emPATH[4], You_IorHeShe_text=emPATH[5], We=emPATH[6], We_text=emPATH[7])

    return outputText


def write():
    global WE
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/main.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(Solitude_Text=invisible_alone() +
                                 I_am_solitude(), Multitude_text=interact()+unity(),
                                 Empathy_Text=render_empath(), Death_text=death(WE))

    with open('output/empathy.html', 'w') as file:
        file.write(outputText)

    pdfkit.from_file('output/empathy.html', 'output/empathy.pdf')


if __name__ == '__main__':
    write()
