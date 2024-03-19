# height of the first shape, this will decrease each time through the loop
myShapeHeight = height()
# how many shapes to draw
myShapeCount = 8
# distance of the offcurve points/handles from the oncurve points
myHandleLength = 100
# how much randomness should there be for the position of the offcurve points
myWobble = 250

# loop through the number of shapes to draw
for myShapeNumber in range(myShapeCount):
    # print the height of this shape
    print(myShapeHeight)
    # create a Bezier path object
    myShape = BezierPath()
    # move the path to the bottom left
    myShape.moveTo((0, 0))
    # draw a line across the bottom to the right
    myShape.lineTo((width(), 0))
    # draw a line up the right side
    myShape.lineTo((width(), myShapeHeight))
    # get two random wobble values, can be negative or positive, to add to the y-coordinates of the off-curve points
    myHandleWobble1 = randint(-myWobble, myWobble)
    myHandleWobble2 = randint(-myWobble, myWobble)
    # draw our big curve
    myShape.curveTo(
        (width(), myShapeHeight + myHandleLength + myHandleWobble1), # handle 1
        (0, myShapeHeight + myHandleLength + myHandleWobble2), # handle 2
        (0, myShapeHeight) # oncurve point
        )

    # set the fill color to random
    # with 30% opacity
    fill(random(), random(), random(), .3)
    # draw our shape
    drawPath(myShape)
    # change the myShapeHeight variable so the next shape will be shorter than the last
    myShapeHeight -= height()/myShapeCount