# make a new page
newPage()

# define my starting coordinates
myX = 0
myY = 0
# define the number of stripes we want to draw, the code will treat it as columns
myCols = 10
# define the width of each stripe; the code will calculate it by dividing the width of the canvas by the number of stripes
myWidth = width()/myCols

# the height of each stripe will be the height of the canvas
myHeight = height()

# define the starting values of red, green, and blue with variables
myRed = 1
myGreen = 0
myBlue = 0

# the code now draws each stripe using a loop; range(myCols) is a sequence that gives us as many numbers as there are between 0 and myCols; myItem is a new temporary variable created by our loop, with each pass it equals the current number in the sequence
for myItem in range(myCols):
    # set the fill color to the present values of the color variables
    fill(myRed, myGreen, myBlue)
    # print the x-coordinate so we can keep track of where we are in the code
    print(myX)
    # draw the rectangle for the stripe on the canvas
    rect(myX, myY, myWidth, myHeight)
    # and now the code increases the value of the x-position; otherwise it will draw all the stripes in the same location
    myX += myWidth
    # the code also increases the amount of green for each stripe it draws
    myGreen += 1/myCols
    
saveImage('stripe_gradient.png')