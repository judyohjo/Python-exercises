'''
Exercise 6 - Output words with length 5 or more (5 inclusive) from the sentence in upper case.
'''

mystring = 'Python is fun and awesome'
new_string = mystring.split()
for i in new_string:
    if len(i) >= 5:
        print(i.upper())
