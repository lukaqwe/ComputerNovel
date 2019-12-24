import re
import random
from decorations import *

#       This file contains all functions needed for
#
#       selecting or cleaning or cutting the text
#


# cleans newlines and other spacey stuff
def clean(string):
    return string.replace('\r', '').replace('\n', ' ').replace('   ', '')


# removes everything which is not alpha at the beginning and changes first letter to uppercase if necessary
def strip(string):
    while not string[0].isalpha() and not string[0] == '<':
        string = string[1:]
    if string[0].islower():
        return string[0].upper() + string[1:]
    return string

# deletes the project gutenberg foreword and afterword


def slice(string):
    foreword = re.compile('[*]{3} START OF THIS PROJECT GUTENBERG .* [*]{3}')
    afterword = re.compile('[*]{3} END OF THIS PROJECT GUTENBERG .* [*]{3}')

    begin = foreword.search(string).end()
    end = afterword.search(string).start()

    return string[begin:end]


# returns a list of senteces that contain a word from input
def onlyWord(string, word):
    Word = re.compile('[ a-zA-Z,\-’\']*' + word + '[ a-zA-Z,\-\'’]*[.?!]{1}')
    return [bold(s, word) for s in Word.findall(clean(string))]


# returns a list of sentences that contain 'I'
def onlyI(string):
    return onlyWord(string, ' I ')


# returns a list of sentences that contain Alice
# This is used only for conversion to other subjects
def onlyAlice(string):
    return onlyWord(string, ' Alice ')


# replaces Alice into I
def AliceToI(string):
    return string.replace('Alice', 'I').replace('herself', 'myself')


# returns true if it matches
def matches(string, expression):
    if re.compile(expression).match(string):
        return True
    return False


# returns true if searches
def search(string, expression):
    if re.compile(expression).search(string):
        return True
    return False


# returns true if the string contains a name
# (actually just an uppercase letter except I)
def hasName(string):
    for i in range(1, len(string)):
        if string[i].isupper() and string[i] != 'I':
            return True
    return False


def decide():
    return random.choice([True, False])


# returns True if it contains 'you'
def hasYou(string):
    return search(string, ' ?[Y,y]ou')


# returns True if it is a chapter name
# unfortunately this does not cover chapter I
def isChapter(string):
    return search(string, '[IVX]{2,10}')


# returns True if it has 'I'
def hasI(string):
    return search(string, ' ?I[\' ]')


# returns True if it has 'I'
def hasHe(string):
    return search(string, ' he[, ]')


# returns True if it has 'I'
def hasShe(string):
    return search(string, ' she[, ]')


# returns True if has 'we'
def hasWe(string):
    return search(string, ' ?[W,w]e ')


# takes as input a list of strings and a number n and outputs
#  a set of n random strings such that they don't repeat
def mix(list, n):
    Set = set()
    while len(Set) != n:
        Set.add(random.choice(list))
    return Set


# converts he to she
def heToShe(string):
    return string.replace('He', 'She').replace(' he ', ' she ').replace(' his ', ' her ').replace(' him ', ' her ').replace(' himself', ' herself')


# converts she to he
def sheToHe(string):
    return string.replace('She', 'He').replace(' she ', ' he ').replace(' her ', ' his ').replace(' her ', ' him ').replace(' herself', ' himself')


# converts I to we
def ItoWe(string):
    return string.replace("I", 'We').replace(' me ', ' us ').replace(' my ', ' our ').replace(' myself', ' ourselves').replace(' am ', ' are ').replace('I,', 'We,').replace('Am ', 'Are ').replace(' was', ' were')


# converts We to I
def weToI(string):
    return string.replace("We ", 'I ').replace(' us ', ' me ').replace(' our ', ' my ')


# converts he to I
def heToI(string):
    return string.replace(' he ', ' I ').replace('He ', 'I ').replace(' him', ' me').replace(' his ', ' my').replace(' himself', ' myself')


def ItoHe(string):
    return string.replace(' I ', ' he ').replace('I ', 'He ').replace(' me', ' him').replace(' my ', ' his ').replace(' myself', ' himself')


def ItoShe(string):
    return sheToHe(ItoHe(string))


def sheToI(string):
    return heToI(sheToHe(string))


def sheOrHeToYou(string):
    string = sheToHe(string)
    return string.replace('He ', 'You ').replace(' he ', ' you ').replace(' himself ', ' yourself').replace(' his ', ' your ').replace(' him ', ' you ')


def collectI(string):
    everyI = [strip(AliceToI(s)) for s in onlyAlice(string)] + onlyI(string)
    return everyI


def collectHe(string):
    everyHe = onlyWord(string,  'He ') + [sheToHe(s) for s in onlyWord(string, 'She ')]
    return everyHe


def collectShe(string):
    everyShe = onlyWord(string, 'She ') + [heToShe(s) for s in onlyWord(string, 'He ')]
    return everyShe


def collectYou(string):
    everyYou = [s for s in onlyWord(string, '[Y,y]ou ') if not hasName(s)]
    everyYou += [sheOrHeToYou(s) for s in collectHe(string)+collectShe(string)]
    return everyYou


def deleteDot(string):
    if string[-1] == '.':
        return string[:-1]
    return string


def conjunction(I, SheHe, length):
    result = []
    while len(result) != length:
        result.append(deleteDot(random.choice(I)) + ' and ' + random.choice(SheHe))
    return result
