__author__ = 'Adel'


def anti_vowel(text):
    output = ""
    for a_char in text:
        if not(a_char in "aeiouAEIOU"):
            output += a_char
    return output

"""  # inefficient way
    for a_char in x:
        if a_char != "a" and a_char != "A" and a_char != "i" and a_char != "I" and a_char != "o" and a_char != "O" and a_char != "u" and a_char != "U" and a_char != "e" and a_char != "E":
            output += a_char

    return output
"""
print anti_vowel("Adiadi")

