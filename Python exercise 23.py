'''
Random() exercise 3 - Print any two random numbers between 0 and the number you input.
'''

import random

number = int(input("Input a number: "))
for i in range(2):
    print("Random number: ", random.randrange(0, number))


