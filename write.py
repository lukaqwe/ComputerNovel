import jinja2
import pdfkit
import sys
import getopt

from dice import *
from colors import *
from tools import decide

WE = False


# this function is contained in this file in order to modify the global variable WE
# it genereates all text from the chapter empathy and returns a tuple of length 8
# the even idexes contain the subchapter names and odd one contain the text itself
def empath():
    global WE

    isHe = decide()

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
        tmp = I_HeShe(isHe=False)
        result[1] = tmp[0]

        if tmp[1]:
            tmp = IorHeShe_IandHeShe(isHe=False)
            result[2] = 'I or She vs I and She'
            result[3] = tmp[0]
            if tmp[1]:
                tmp = You_IorHeShe(isHe=False)
                result[4] = 'You vs I or She'
                result[5] = tmp[0]
                if tmp[1]:
                    result[6] = 'We'
                    result[7] = we()
                    WE = True
    return result


# this function is used to generate the chapter empathy from the template empath.html
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


# this is the main function that does the writing itself
def write(iterations=0, PDF=True):
    global WE
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/main.html"
    template = templateEnv.get_template(TEMPLATE_FILE)

    if iterations == 0:
        outputText = template.render(Solitude_Text=invisible_alone() +
                                     I_am_solitude(), Multitude_text=interact()+unity(),
                                     Empathy_Text=render_empath(), Death_text=death(WE))
        with open('output/empathy.html', 'w') as file:
            file.write(outputText)
        if PDF:
            pdfkit.from_file('output/empathy.html', 'output/empathy.pdf')
    else:
        for i in range(iterations):
            outputText = template.render(Solitude_Text=invisible_alone() +
                                         I_am_solitude(), Multitude_text=interact()+unity(),
                                         Empathy_Text=render_empath(), Death_text=death(WE))
            with open('output/empathy' + str(i) + '.html', 'w') as file:
                file.write(outputText)
            if PDF:
                pdfkit.from_file('output/empathy' + str(i) + '.html',
                                 'output/empathy' + str(i) + '.pdf')


# this is used only to parse the command line arguments
def main(argv):
    iter = 0
    pdf = True
    try:
        opts, args = getopt.getopt(argv, "i:p", ["iterations=", "pdf="])
    except getopt.GetoptError:
        print('Cannot parse the command.\nCheck user manual. \nExiting ...')
        sys.exit(2)
    if len(argv) == 0:
        write()
        sys.exit(0)
    for opt, arg in opts:
        if opt == '--iterations':
            iter = int(arg)
        if opt == '-i':
            iter = int(arg)
        if opt == '-p':
            pdf = False
        if opt == '--pdf':
            if arg == 'False':
                pdf = False

    write(iter, pdf)


if __name__ == "__main__":
    main(sys.argv[1:])
