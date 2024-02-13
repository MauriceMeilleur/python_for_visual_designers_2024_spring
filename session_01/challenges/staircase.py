# define how many steps to draw
myStepCount = 20
# define the width of the steps to be the full width of the canvas divided by the step count; remember that the default width() is 1000
myWidth = width()/myStepCount
# define the height of the steps the same way
myStepHeight = height()/myStepCount

# the staircase will be a series of rectangles that get taller; this variable controls the height of each rectangle—starting at the height of the first step
myHeight = myStepHeight

# the rectangles will be drawn one after another, shifting their horizontal positions; this variable will define those positions
myX = 0

# create a new canvas
newPage()
# set the fill color to green
fill(0, 1, 0)
# draw the background: a rectangle that starts at (0, 0) and covers the whole canvas
rect(0, 0, width(), height())
# now set the fill color to magenta for the steps
fill(1, 0, 1)
# now the code will loop through the range of numbers 0–myStepCount
for myRect in range(myStepCount):
    # draw a rectangle with the current myWidth and myHeight values
    rect(myX, 0, myWidth, myHeight)
    # increase the x-position so that the next rectangle is drawn to the right
    myX += myWidth
    # also augment myHeight value, so the next rectangle will be taller by the same amount
    myHeight += myStepHeight
    
saveImage('staircase.png')