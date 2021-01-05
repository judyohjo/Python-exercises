'''
Exercise 25 - Randomly pick a word from a sentence and see if it's a vowel.
'''

import random

string = input("Input a phrase/sentence: ")
vowel = 'a, e, i, o, u'
random_num = random.randrange(0, len(string)-1)
random_alphabet = string[random_num]

if random_alphabet in vowel:
    print("This alphabet, " + random_alphabet + ", is a vowel.")
else:
    print("This alphabet, " + random_alphabet + ", is not a vowel.")

