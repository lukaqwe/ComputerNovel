from read import *
from tools import *
from math import fabs


isShe = decide()
isHe = not isShe

everyI = [strip(s) for s in onlyI(InvisibleMan) if not search(
    s, ' [I,i]nvisible') and not hasName(s) and not hasYou(s) and not hasHe(s) and not hasShe(s) and not hasWe(s)]
battles = int((len(everyI)//ratio())//2)


def I_HeShe():
    global Alice, LookingGlass, TimeMachine, isHe, battles

    # collecting the I senteces
    everyI = collectI(Alice+LookingGlass+TimeMachine)

    gap = battles // ratio()
    result = ''

    if isHe:
        # collecting the he senteces
        everyHe = collectHe(Alice+LookingGlass+TimeMachine)

        # keeping track of the 'battle'
        countI = 0
        countHe = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyI) + '<br>'
                countI += 1
            else:
                result += random.choice(everyHe) + '<br>'
                countHe += 1

        battles += int(fabs(countI-countHe))
        return result, fabs(countI-countHe) <= gap
    else:  # Do the exact same thing but with She
        everyShe = collectShe(Alice+LookingGlass+TimeMachine)

        # keeping track of the 'battle'
        countI = 0
        countShe = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyI) + '<br>'
                countI += 1
            else:
                result += random.choice(everyShe) + '<br>'
                countShe += 1

        battles += int(fabs(countI-countShe))
        return result, fabs(countI-countShe) <= gap


def IorHeShe_IandHeShe():
    global Alice, LookingGlass, TimeMachine, isShe, battles

    everyI = [strip(s) for s in collectI(Alice+LookingGlass+TimeMachine)]

    gap = battles // ratio()
    result = ''

    if isShe:
        everyShe = collectShe(Alice+LookingGlass+TimeMachine)
        everyIandShe = conjunction(everyI, everyShe, 200)

        # keeping track of the battle
        countIorShe = 0
        countIandShe = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyI + everyShe) + '<br>'
                countIorShe += 1
            else:
                result += random.choice(everyIandShe) + '<br>'
                countIandShe += 1

        battles += int(fabs(countIandShe-countIorShe))
        return result, fabs(countIandShe-countIorShe) <= gap
    else:  # Do the exact same thing but with He
        everyHe = collectHe(Alice+LookingGlass+TimeMachine)
        everyIandHe = conjunction(everyI, everyHe, 200)

        # keeping track of the battle
        countIorHe = 0
        countIandHe = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyI + everyHe) + '<br>'
                countIorHe += 1
            else:
                result += random.choice(everyIandHe) + '<br>'
                countIandHe += 1

        battles += int(fabs(countIandHe-countIorHe))
        return result, fabs(countIandHe-countIorHe) <= gap


def You_IorHeShe():
    global Alice, LookingGlass, TimeMachine, isHe, battles

    gap = battles // ratio()

    everyI = [strip(s) for s in collectI(Alice+LookingGlass+TimeMachine)]
    everyYou = [strip(s) for s in collectYou(Alice+LookingGlass+TimeMachine)]

    result = ''

    if isHe:
        everyHe = collectHe(Alice+LookingGlass+TimeMachine)
        everyIorHe = everyHe + everyI

        countIorHe = 0
        countYou = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyIorHe) + '<br>'
                countIorHe += 1
            else:
                result += random.choice(everyYou) + '<br>'
                countYou += 1

        return result, fabs(countYou-countIorHe) <= gap

    else:  # Do the exact same thing but with She
        everyShe = collectShe(Alice+LookingGlass+TimeMachine)
        everyIorShe = everyShe + everyI

        countIorShe = 0
        countYou = 0

        for i in range(battles):
            if decide():
                result += random.choice(everyIorShe) + '<br>'
                countIorShe += 1
            else:
                result += random.choice(everyYou) + '<br>'
                countYou += 1

        return result, fabs(countYou-countIorShe) <= gap
