myvar = 4
mylist = [1, 2, 3, myvar]
print(mylist)
# slice
print(mylist[0:3])

myList = [100, 200, 300, 400]
print(myList[0:2])

# add a new variable to the end of the list
myvar = "NEW"
mylist.append(myvar)
print(mylist)

# insert a new variable into a list
mylist.insert(0, myvar)
print(mylist)
# removes last item from the list
item_removed = mylist.pop()
print(mylist)
#  remove the element in that index no
mylist.pop(3)
mylist.reverse()
# removes a specific value from the list
mylist.remove(4)
print(mylist)
mylist.pop()
mylist.insert(0, 5)
mylist.insert(1, 6)
print(mylist)
mylist.sort()
mylist.reverse()
print(mylist)

unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
unsorted_list.sort()
print(unsorted_list)
print(unsorted_list[0:3])
