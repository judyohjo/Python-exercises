'''
Exercise 11 - Input a number and print the number of times of "X" (eg. if number is 3, print...
X
XX
XXX)
'''

num = int(input("Input a number: "))
for i in range(1, num+1):
    print(i*"X")


