from read import *
from tools import *
from math import fabs


isShe = decide()
isHe = not isShe


def I_HeShe():
    global Alice, LookingGlass, TimeMachine, isHe

    # collecting the I senteces
    everyI = collectI(Alice+LookingGlass+TimeMachine)

    battles = 30
    gap = battles // 10
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

        return result, fabs(countI-countShe) <= gap


def IorHeShe_IandHeShe():
    global Alice, LookingGlass, TimeMachine, isShe

<<<<<<< HEAD
    everyI = [s for s in collectI(Alice+LookingGlass+TimeMachine)]
=======
    everyI = [strip(s) for s in collectI(Alice+LookingGlass+TimeMachine)]
>>>>>>> master

    battles = 30
    gap = battles // 10
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

        return result, fabs(countIandHe-countIorHe) <= gap


def You_IorHeShe():
    global Alice, LookingGlass, TimeMachine, isHe

    battles = 30
    gap = battles // 10

<<<<<<< HEAD
    everyI = [s for s in collectI(Alice+LookingGlass+TimeMachine)]
    everyYou = [s for s in collectYou(Alice+LookingGlass+TimeMachine)]
=======
    everyI = [strip(s) for s in collectI(Alice+LookingGlass+TimeMachine)]
    everyYou = [strip(s) for s in collectYou(Alice+LookingGlass+TimeMachine)]
>>>>>>> master

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
