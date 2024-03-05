# set the blend mode to overlay to let the shapes overlap
blendMode('overlay')

# set up some variables for the circles
myShapeSize = 250 # size
myRadius = 250 # how far to draw each circle from the center of the canvas
myShapeCount = 15 # how many circles to draw

# shift the origin to the center of the canvas
translate(width()/2, height()/2)

# loop through the number of shapes we will draw
for myShape in range(myShapeCount):
    # define a random fill
    fill(random(), random(), random())
    # draw the circle
    # the x and y will be minus half the shape size
    # but y will also be offset by the radius, so that when the code rotates the canvas, the circles will always be a fixed distance from the center
    oval(-myShapeSize/2, -myShapeSize/2+myRadius, myShapeSize, myShapeSize) 
    # rotate the canvas by the increment 360/myShapeCount, so that there will be a complete rotation when all the circles are drawn
    rotate(360/myShapeCount)
    
saveImage('circleOfCircles.png')