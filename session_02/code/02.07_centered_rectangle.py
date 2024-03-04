# set a variable for the size of our shape
myShapeSize = 500

# translate() is a DrawBot function that changes the position of the origin (x = 0, y = 0) on the canvas for everything drawn after it is called
# you can also use it to change the position of BezierPaths, but we'll talk about that later!
# here we'll use the function to move the origin from the default lower left corner of the canvas to the center of the canvas
translate(width()/2, height()/2)
# with the origin in its new position, we'll draw a rectangle
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)