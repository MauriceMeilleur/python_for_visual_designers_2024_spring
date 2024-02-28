# create a string variable
myString = 'the quick brown fox'

# set the font size
fontSize(130)
# loop through each character (element) in our string
for myLetter in myString:
    # define two variables for random horizontal and vertical positions on the canvas
    # randint is a Python function that takes two arguments: a starting integer and an ending integer; it returns a random integer between them
    # width() and height() are DrawBot functions that take no arguments; they return the width and height in units of the current canvas
    myX = randint(0, width())
    myY = randint(0, height())
    # random() is a Python function that returns a random number between 0 and 1
    # we can call it three times to get three random numbers for red, green, and blue values for fill(), which also have to be between 0 and 1; when we do this the fill color will be random
    fill(random(), random(), random())
    # draw our text to the canvas at the random x, y coordinates we defined earlier in the loop
    text(myLetter, (myX, myY))
    