'''
Get the smallest number from each list and create a new list and print that new list.
'''

list1 = [1, 3, 5, 0, 2, 3]
list2 = [3, 5, 3, 56, 7, 22]
list3 = [67, 34, 24, 15, 88, 99]

newlist = []

smallest1 = min(list1)
smallest2 = min(list2)
smallest3 = min(list3)

newlist.append(smallest1)
newlist.append(smallest2)
newlist.append(smallest3)

print(newlist)
