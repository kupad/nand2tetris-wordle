import re
import random

MAX_WORDS = 1000

dictpath = '/usr/share/dict/american-english'


def main():
    words = []
    widx = 0
    with open(dictpath, 'r') as dfile:
        for line in dfile:
            word = line[0:-1]
            if re.match(r'^[a-z]{5}$', word):
                words.append(word)

    random.shuffle(words)
    words = words[0:MAX_WORDS]

    code = []
    for widx, word in enumerate(words):
        code.append(f'\tlet WORDS[{widx}] = "{word.upper()}";')

    with open('Dictionary.template', 'r') as templatef:
        template = templatef.read()

    out = (template
           .replace('XXX_SIZE_XXX', str(len(code)))
           .replace('XXX_WORDS_XXX', '\n'.join(code)))
    print(out)


main()
