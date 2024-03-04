# create a list
myGroceryList = ['apples', 'oranges', 'bananas']

# set a starting point for x and y
myX = 500
myY = 100
# get a random value and store it in a variable for the fill alpha
myRandomAlpha = random()
print('random alpha:', myRandomAlpha)
# set the font size for everything we're going to draw on the canvas
fontSize(100)

for myGroceryItem in myGroceryList:
    # the code inside this loop runs as many times as there are elements in myGroceryList
    print(myGroceryItem)
    # now a nested for-loop will run through every character in the string that is the current grocery list element
    for myChar in myGroceryItem:
        # the code inside *this* loop runs once for every character in the current myGroceryList element
        print(myChar)
        # set the fill to a random color, but use the alpha we calculated before we started any loops
        fill(random(), random(),random(), myRandomAlpha)
        # draw the text to canvas at the x, y coordinates we defined earlier
        text(myChar, (myX, myY))
        # increase the y coordinate for each letter
        myY += 40
        print(myY)
    # note the dedent, now we have exited the character for-loop and we're back to the code that runs once for every myGroceryList item
    # augment the X variable
    myX += 40
    
# now the code is outside both loops
print('we are done with the loop')