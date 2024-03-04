# define a variable to store a value we'll use to change the size of the shapes we're going to draw
myScaleValue = .9
# define another variable to size the stroke on the shapes with the value of the first stroke
myStrokeWidth = 5
# define our shape size; the stroke will straddle the path of the shape; so if we want to show the full stroke at the shape's largest size, we need to make it slightly smaller than the canvas
myShapeSize = width() - myStrokeWidth
# move the origin to the center of the canvas
translate(width()/2, height()/2)
# set the stroke color to red
stroke(1, 0, 0)
# set the fill color to None = no fill
fill(None)
# now the code will for-loop 50 times and draw a shape each time
for myNumber in range(50):
    # set the stroke width; we'll do this each pass because we're going to adjust it each loop 
    strokeWidth(myStrokeWidth)
    print(myStrokeWidth)
    # draw a centered rectangle
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    # scale the canvas by our scale value
    scale(myScaleValue)
    # now we're going to offset the effect of scaling on our stroke width in order to keep it optically constant; we'll do this by increasing it by our scale value each time
    # since our scale value is less than 1, dividing by that value will increase it
    myStrokeWidth /= myScaleValue