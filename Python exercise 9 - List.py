'''
Exercise 9 - Calculate the sum and average of list of numbers.
'''

list1 = ['6', '32', '15', '22', '5']
total = 0
for i in list1:
    total += int(i)

print("Sum:", total)
print("Average:", (total/len(list1)))

