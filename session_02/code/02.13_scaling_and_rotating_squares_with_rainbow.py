# we want to use HSV for color, but we'll have to convert it to RGB
# so we're going to import a function from a module of code—to import means we make code in a module/library available in the module (DrawBot) we're working in
# normally we keep modules/libraries separate in order to keep projects manageable
from colorsys import hsv_to_rgb

# set our starting hue, saturation, and value numbers; we're really only interested in hue for this sketch
myHue = 0
mySat = 1
myVal = 1

myShapeSize = width() # how large to draw our squares 
mySquareCount = 25 # how many squares we'll draw
myScaleValue = .9 # how much to scale the squares each time we draw them
myRotateValue = 5 # how many degrees to rotate a square each time we draw one

# now we'll define a variable to use to toggle between True and False
myToggle = True

# move the origin to the center of the canvas
translate(width()/2, height()/2)

# now we'll start a for-loop to draw all the squares
for myNumber in range(mySquareCount):    
    # if the current value of myToggle is True, run this code block that sets the fill to black and sets the value of myToggle to False
    if myToggle:
        fill(0)
        myToggle = False
    # but if the current value of myToggle is False, run this code block that does two things:
    # it sets the rgb fill color using the hsv_to_rgb() function and tha value of myHue
    # and it sets the value of myToggle to True
    else:
        print(hsv_to_rgb(myHue, mySat, myVal))
        # * is a Python operator that 'unpacks' the elements of a sequence; hsv_to_rgb returns a sequence that has to be unpacked into 3 values so we can use it for fill()
        fill(*hsv_to_rgb(myHue, mySat, myVal))
        myToggle = True
    # now the code will draw a centered rectangle, using the present values of fill, myScaleValue, and myRotateValue
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    # the code then scales the canvas
    scale(myScaleValue)
    # … and rotates the canvas
    rotate(myRotateValue)
    # … and changes the hue by a fraction of the total 360º of hue defined by mySquareCount
    myHue += 1/mySquareCount
    print('myHue is', myHue)