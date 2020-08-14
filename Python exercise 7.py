'''
Count the number of vowels in a string.
'''

mystring = 'Python is fun and awesome'
new_string = mystring.split()
count = 0
for i in new_string:
    for x in i:
        if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
            count+=1
print(count)
