'''
Remove the duplicated number from the list (ie. list1 = [3, 4, 5, 2, 3, 6, 4, 10],
then output [3, 4, 5, 2, 6, 10])
'''

list1 = [3, 4, 5, 2, 3, 6, 4, 10]
newlist = []
for i in list1:
    if i in newlist:
        pass
    else:
        newlist.append(i)

print(newlist)


