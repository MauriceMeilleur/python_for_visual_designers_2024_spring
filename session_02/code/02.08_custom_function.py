# we're going to create a custom function that will center a rectangle on the canvas with its origin at its center 
# this function will take two required arguments: width (myW) and height (myH)
def myCenteredRect(myW, myH):
    print('this is a centered rectangle', myW, myH)
    # remember that DrawBot draws from the lower left, so to center the shape, we have to draw it from a point shifted left and down by half its dimensions
    rect(-myW/2, -myH/2, myW, myH)
    
# let DrawBot create a newPage() with its defaul dimensions, and move the origin to the center of the page
translate(width()/2, height()/2)
# draw the centered rectangle with our custom function, and leave the fill at its default value
myCenteredRect(500, 500)
# now set the fill color to red
fill(1, 0, 0)
# and draw another centered rectangle on top with our function
myCenteredRect(250, 100)