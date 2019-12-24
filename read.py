from tools import slice

Adventures = ''
Memoirs = ''
Alice = ''
LookingGlass = ''
InvisibleMan = ''
Dracula = ''
Frankenstein = ''
TimeMachine = ''

with open("lib/AdventuresOfSherlockHolmes.txt", 'r') as Adventures_file:
    Adventures = slice(Adventures_file.read())
with open('lib/MemoirsOfSherlockHolmes.txt', 'r') as Memoirs_file:
    Memoirs = slice(Memoirs_file.read())
with open('lib/AliceInWonderland.txt', 'r', encoding='utf8', errors='ignore') as Alice_file:
    Alice = slice(Alice_file.read())
with open('lib/ThroughTheLookingGlass.txt', 'r') as LookingGlass_file:
    LookingGlass = slice(LookingGlass_file.read())
with open('lib/TheInvisibleMan.txt', 'r') as InvisibleMan_File:
    InvisibleMan = slice(InvisibleMan_File.read())
with open('lib/Dracula.txt', 'r') as Dracula_file:
    Dracula = slice(Dracula_file.read())
with open('lib/Frankenstein.txt', 'r') as Frankenstein_file:
    Frankenstein = slice(Frankenstein_file.read())
with open('lib/TimeMachine.txt', 'r') as TimeMachine_file:
    TimeMachine = slice(TimeMachine_file.read())
