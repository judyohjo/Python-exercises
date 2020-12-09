'''
Exercise 13 - Get the biggest number from each list and get the smallest number from each list and calculate the difference. 
Then, create a new list and get the average of those numbers (2dp).
'''

list1 = [1, 3, 5, 0, 2, 3]
list2 = [3, 5, 3, 56, 7, 22]
list3 = [67, 34, 24, 15, 88, 99]

newlist = []

difference1 = max(list1) - min(list1)
difference2 = max(list2) - min(list2)
difference3 = max(list3) - min(list3)

newlist.append(difference1)
newlist.append(difference2)
newlist.append(difference3)

total = difference1 + difference2 + difference3

print("New list:", newlist)
print("Average of the difference: {:.2f}".format(total/len(newlist)))
