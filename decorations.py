import random
import re


def splash():
    bucket = ['<b>', '<strong>', '<i>', '<em>', '<mark>',
              '<small>', '<del>', '<ins>', '<sub>',  '<sup>']
    one = random.choice(bucket)
    return (one, '</' + one[1:])


def bold(string, word):  # word is a REGEX
    begin = re.search(word, string).start()
    end = begin+1
    while string[end].isalpha():
        end += 1
    return string[:begin] + '<b>' + string[begin:end] + '</b>' + string[end:]
