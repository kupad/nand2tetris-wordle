import re

MAX_WORDS = 1000

dictpath = '/usr/share/dict/american-english'


def main():
    words = []
    widx = 0
    with open(dictpath, 'r') as dfile:
        for line in dfile:
            word = line[0:-1]
            if re.match(r'^[a-z]{5}$', word):
                words.append(f'\tlet WORDS[{widx}] = "{word.upper()}";')
                widx += 1
                if widx >= MAX_WORDS:
                    break

    with open('Dictionary.template', 'r') as templatef:
        template = templatef.read()

    out = (template
           .replace('XXX_SIZE_XXX', str(widx-1))
           .replace('XXX_WORDS_XXX', '\n'.join(words)))
    print(out)


main()
