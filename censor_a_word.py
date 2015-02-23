__author__ = 'Adel'


def censor(text, word):
    text = text.split()
    asterisk_word = "*" * len(word)

    for i, a_word in enumerate(text):
        if a_word == word:
            text[i] = asterisk_word
    text = " ".join(text)
    return text

print censor("ja sam car of svih krokodila", "svih")