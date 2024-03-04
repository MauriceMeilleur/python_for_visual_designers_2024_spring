# let's define a custom function just like the last sketch
def myCenteredRect(myW, myH):
    print('this is a centered rectangle', myW, myH)
    rect(-myW/2, -myH/2, myW, myH)

# savedState() is a DrawBot function that allows us to write code outside the present state of the canvas, that won't affect it
# think of savedState() like Las Vegas: what happens in Vegas, stays in Vegas
with savedState():
    # let's move the origin to the center
    translate(width()/2, height()/2)
    # now we'll call our custom function to draw a rectangle
    myCenteredRect(500, 500)
    # now we'll change the fill color
    fill(1, 0, 0)
    # and draw another rectangle with our function
    myCenteredRect(250, 250)
    # and do those both again
    fill(0, 1, 0)
    myCenteredRect(320, 150)

# by dedenting we exit the saved state and go back to the original state of the canvas, its settings preserved
# no translation or change of fill color
oval(0, 0, 500, 500)