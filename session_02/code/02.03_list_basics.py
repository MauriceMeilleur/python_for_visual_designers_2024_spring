# create a list of strings
myGroceryList = ['apples', 'oranges', 'bananas']

# give us the length
print('length:', len(myGroceryList))

# 'slice' the list to give us a particular item; list indices begin with 0 because computers start counting with 0, so index [2] will give us the third element in the list
print('third item:', myGroceryList[2])

# slice a portion of the list; [:2] will give us the first two elements from the list; think of ':' as meaning 'up to', not 'up to and including'
print('first two items:', myGroceryList[:2])
# index [-1] in a list is the last element
# [-2:] will give us the last two elements from the list
print('last two items:', myGroceryList[-2:])

# make an alphabetical copy of a sorted list
# sorted() is a Python function that returns a sorted version of a list; the original list remains unchanged
# NB: A–Z come before a–z
# here we define a variable and give it the value of that sorted version—anything we do to that copy will not affect the original
mySortedList = sorted(myGroceryList)
print('a sorted copy:', mySortedList)

# sort a list in place
# [listname].sort() is a Python function that sorts the original list; the original stays changed
myGroceryList.sort(reverse=True)
print('the sorted original:', myGroceryList)