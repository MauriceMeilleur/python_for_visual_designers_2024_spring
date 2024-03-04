# center a rectangle of random color on a series of pages

for myNumber in range(10): # loop through 10 numbers
    # make a new page
    newPage(500, 1000) 
    # set a random color
    fill(random(), random(), random()) 
    # draw a shape that’s half the width of the canvas; we'll define it here since if we called width() *before we set up the newPage() we'd get the default width of a canvas in DrawBot
    myShapeWidth = width()/2
    # figure out the total horizontal margins by subtracting the shape width from the canvas width
    myXMargin = width() - myShapeWidth
    # to center the object, we would want an equal margin on both its sides, so its left offset would be half the total margin
    myXOffset = myXMargin/2
    # draw the rectangle
    rect(myXOffset, 0, myShapeWidth, height()/2)
# save the file (note the dedent!)
saveImage('randomColors.gif') 