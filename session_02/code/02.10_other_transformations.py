# set a shape size
myShapeSize = 800

# move the origin to the center of the canvas
translate(width()/2, height()/2)
# rotate() is a DrawBot function that requires one argument, the degrees of the angle of rotation; by default rotation happens around the present origin, but you can add an argument (x, y) to change the axis point of the rotation
rotate(0)
# skew() is a DrawBot function that distorts the shape of the canvas; if you pass it one argument (degrees) it distorts the canvas along the x dimension; if you pass two, the function will distort the x and y dimensions
skew(15)
# scale() is a DrawBot function that compresses or expands the canvas (1 = 100%); it can take one argument (for scale along both the x and y dimensions) or separate x and y values
scale(.5, 1)
# draw a centered rectangle on our transformed canvas
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
# change the fill color to green
fill(0, 1, 0)
# set the font size
fontSize(100)
# draw some text on the canvas to help show the transformations
text('hello world', (0, 0))