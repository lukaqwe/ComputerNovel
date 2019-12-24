from read import *
from tools import *


feigenbaum = 4.66920160910299


# returns sentences that contain 'invisible' and 'alone'
def invisible_alone():
    global InvisibleMan
    everyInvisible = [s for s in onlyWord(
        InvisibleMan, ' [I,i]nvisible') + onlyWord(InvisibleMan, ' [A,a]?lone') if not hasYou(s) and not isChapter(s) and not hasName(s)]
    InvisibleI = [heToI(s) for s in everyInvisible]
    return "<br>".join(mix(InvisibleI, len(InvisibleI)//feigenbaum))


# returns senteces that contain I form the Invisible Man
def I_am_solitude():
    global InvisibleMan
    everyI = [s for s in onlyI(InvisibleMan) if not search(
        s, ' [I,i]nvisible') and not hasName(s) and not hasYou(s) and not hasHe(s) and not hasShe(s) and not hasWe(s)]
    return ' '.join(mix(everyI, len(everyI)//(feigenbaum*2)))


# returns sentences that contatin the word speak and ask
def interact():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
<<<<<<< HEAD
    everySpeak = [s for s in onlyWord(Texts, ' speak') + onlyWord(Texts, ' spoke') + onlyWord(Texts, ' ask')
=======
    everySpeak = [strip(s) for s in onlyWord(Texts, ' speak') + onlyWord(Texts, ' spoke') + onlyWord(Texts, ' ask')
>>>>>>> master
                  if not hasName(s) and (hasYou(s) or hasHe(s) or hasShe(s) or hasWe(s))]
    return '<br>'.join(mix(everySpeak, len(everySpeak)//feigenbaum))


# returns sentences that contain the word both and together
def unity():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
<<<<<<< HEAD
    everyBoth = [s for s in onlyWord(Texts, ' both') +
=======
    everyBoth = [strip(s) for s in onlyWord(Texts, ' both') +
>>>>>>> master
                 onlyWord(Texts, ' together') if not hasName(s)]
    return ' '.join(mix(everyBoth, len(everyBoth)//feigenbaum))


# returns I sentences from Invisible Man converted to a we
def we():
<<<<<<< HEAD
    everyWe = [ItoWe(s) for s in onlyI(InvisibleMan) if not hasName(s)
=======
    everyWe = [ItoWe(strip(s)) for s in onlyI(InvisibleMan) if not hasName(s)
>>>>>>> master
               and not hasYou(s) and not hasHe(s) and not hasShe(s)]
    return '<br>'.join(mix(everyWe, len(everyWe)//feigenbaum))


# prints sentences which contain the word 'death' from Frankenstein and Dracula
def death(we=False):
    global Frankenstein, Dracula
    AllDeath = onlyWord(Frankenstein+Dracula, ' ?[D,d]eath')
<<<<<<< HEAD
    everyDeath = [s for s in AllDeath if not hasName(s)]  # len = 107
=======
    everyDeath = [strip(s) for s in AllDeath if not hasName(s)]  # len = 107
>>>>>>> master
    everyIdeath = [sheToI(heToI(weToI(s))) for s in everyDeath]
    if we:
        return '<br>'.join([ItoWe(s) for s in mix(everyDeath, len(everyDeath)//feigenbaum) if not hasShe(s) and not hasHe(s)]+['We died.'])
    else:
<<<<<<< HEAD
        return '<br>'.join(list(mix(everyIdeath, len(everyIdeath)//feigenbaum))+['I died.'])
=======
        return '<br>'.join(list(mix(everyIdeath, len(everyIdeath)//feigenbaum))+['<b>I died.</b>'])
>>>>>>> master
