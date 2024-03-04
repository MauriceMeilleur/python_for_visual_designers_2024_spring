# again, we'll import the hue/saturation/value conversion function from the colorsys library
from colorsys import hsv_to_rgb

# and set our initial hue/saturation/value numbers
myHue = 0 # red in the HSV model
mySat = 1 # fully chromatic
myVal = 1 # full brightness

myShapeSize = width() # how large to draw our squares 
mySquareCount = 25 # how many squares we'll draw
myScaleValue = .9 # how much to scale the squares each time we draw them
myRotateValue = 5 # how many degrees to rotate a square each time we draw one
# our toggle variable
myToggle = True

myFrameCount = 90 # how many frames to draw

# a for-loop through our frames
for myFrameNumber in range(myFrameCount):
    # the code at this indent level runs once per page/frame
    # create a new page
    newPage()
    # move the origin to the center of the page
    translate(width()/2, height()/2)

    # now loop through our square count to draw our squares
    for myNumber in range(mySquareCount):
        # code at this indent level runs once per shape, per page
        # if myToggle is True, the fill is black
        if myToggle:
            fill(0)
            # change myToggle to False so the next fill will be a color
            myToggle = False
        # if myToggle is False, set the fill to our HSV color, converted to RGB
        else:
            print('converted to rgb:', hsv_to_rgb(myHue, mySat, myVal))
            fill(*hsv_to_rgb(myHue, mySat, myVal))
            # change myToggle to True so the next fill will be black
            myToggle = True
        # now that fill is defined and myToggle is set properly, draw our centered rectangle
        rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
        # scale the canvas down
        scale(myScaleValue)
        # rotate the canvas
        rotate(myRotateValue)
    
        # each time we've drawn a shape, we change the hue
        # by setting it to 1/mySquareCount, the value will increase by 1 over the course of the total loop of mySquareCount
        myHue += 1 / mySquareCount
        print('myHue is', myHue)

    # note the dedent, we're outside the nested for-loop, this code again only runs once per frame
    # set the rotate value so that it will rotate a full 360º over the course of the animation
    myRotateValue += 360/myFrameCount
    
# save all the pages/frames as a gif
saveImage('rotatingSquares.gif')