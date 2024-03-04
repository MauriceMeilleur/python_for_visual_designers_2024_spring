# remember all the code at this level of indentation is run once

# create a list
myGroceryList = ['apples', 'oranges', 'bananas']

# set a starting point for x and y
myX = 500
myY = 100
# get a random alpha value and store it in a variable
myRandomAlpha = random()
print('random alpha:', myRandomAlpha)

# for-loop through the elements in the grocery list
for myGroceryItem in myGroceryList:
    # the loop will set the control variable to the value of each element in myGroceryList in order
    print(myGroceryItem)
    # because there are 3 elements in myGroceryList, the code insidet this loop runs three times   
    # set the font size
    fontSize(100)
    # set the fill to a random color, and we'll use the alpha value we calculated before we started the for-loop
    fill(random(), random(),random(), myRandomAlpha)
    # draw the text on the canvas at the x and y coordinates we defined
    text(myGroceryItem, (myX, myY))
    # augment the myY variable so it increases every loop
    myY += 100
    print('myY:', myY)     
# note the dedent
print('done with the loop!')    

# the last value of the control variable is still in memory
print(myGroceryItem)