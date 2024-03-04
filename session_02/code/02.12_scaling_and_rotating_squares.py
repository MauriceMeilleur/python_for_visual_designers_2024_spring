mySquareCount = 50 # how many squares to draw
myScaleValue = .9 # how much to scale the squares each loop
myRotateValue = 4 # how much to rotate the squares each loop
myShapeSize = width() # the size of the first square

# shift the origin to the center of the canvas
translate(width()/2, height()/2)

# now loop through the numbers 0–mySquareCount
for myNumber in range(mySquareCount):
    # set a random fill color
    fill(random(), random(), random()) 
    # draw a rectangle at the center of the canvas
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    # scale the canvas by our scale value
    scale(myScaleValue)
    # rotate the canvas by our rotation 
    rotate(myRotateValue)