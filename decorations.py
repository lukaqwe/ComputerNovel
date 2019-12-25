import random
import re

# TO be added More


def bold(string, word):  # word is a REGEX
    begin = re.search(word, string).start()
    end = begin+1
    while string[end].isalpha():
        end += 1
    return string[:begin] + '<b>' + string[begin:end] + '</b>' + string[end:]
