'''
Count the number of vowels in a string.
'''

mystring = 'Python is fun and awesome'
count = 0
vowels = 'aeiou'
for i in mystring:
    if i in vowels:
        count+=1
print(count)
