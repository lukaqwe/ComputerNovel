from read import *
from tools import *


# collects sentences that contain 'invisible' and 'alone'
def invisible_alone():
    global InvisibleMan
    everyInvisible = [strip(s) for s in onlyWord(
        InvisibleMan, ' [I,i]nvisible') + onlyWord(InvisibleMan, ' [A,a]?lone') if not isChapter(s) and not hasName(s)]
    InvisibleI = [heToI(s) for s in everyInvisible]
    return "<br>".join(mix(InvisibleI, len(InvisibleI)//ratio())) + "<br>"


# collects senteces that contain I f
def I_am_solitude():
    global InvisibleMan
    everyI = [strip(s) for s in onlyI(InvisibleMan) if not search(
        s, ' [I,i]nvisible') and not hasName(s) and not hasYou(s) and not hasHe(s) and not hasShe(s) and not hasWe(s)]
    return '<br>'.join(mix(everyI, len(everyI)//(ratio())))


# collects sentences that contatin the word speak and ask from Sherlock Holmes texts
def interact():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
    everySpeak = [strip(s) for s in onlyWord(Texts, ' speak') + onlyWord(Texts, ' spoke') + onlyWord(Texts, ' ask')
                  if not hasName(s) and (hasYou(s) or hasHe(s) or hasShe(s) or hasWe(s))]
    return '<br>'.join(mix(everySpeak, len(everySpeak)//ratio()))


# collects sentences that contain the word both and together from Sherlock Holmes texts
def unity():
    global Memoirs, Adventures
    Texts = Memoirs + Adventures
    everyBoth = [strip(s) for s in onlyWord(Texts, ' both') +
                 onlyWord(Texts, ' together') if not hasName(s)]
    return '<br>'.join(mix(everyBoth, len(everyBoth)//ratio()))


# collects I sentences from Invisible Man converted to a we
def we():

    everyWe = [ItoWe(strip(s)) for s in onlyI(InvisibleMan) if not hasName(s)
               and not hasYou(s) and not hasHe(s) and not hasShe(s)]
    return '<br>'.join(mix(everyWe, len(everyWe)//ratio()))


# collects sentences which contain the word 'death' from Frankenstein and Dracula
def death(we=False):
    global Frankenstein, Dracula
    AllDeath = onlyWord(Frankenstein+Dracula, ' ?[D,d]eath')

    everyDeath = [strip(s) for s in AllDeath if not hasName(s)]
    everyIdeath = [sheToI(heToI(weToI(s))) for s in everyDeath]
    if we:
        return '<br>'.join([ItoWe(s) for s in mix(everyDeath, len(everyDeath)//ratio())]+['We died.'])
    else:
        return '<br>'.join(list(mix(everyIdeath, len(everyIdeath)//ratio()))+['<b>I died.</b>'])
