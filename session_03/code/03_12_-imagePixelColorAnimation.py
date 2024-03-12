# a two-phase animation of the imagePixelColor vector simplification

myImageName = 'Juvenile_Ragdoll.jpg'
myXCount, myYCount = 10, 10
# set the number of frames
myFrameCount = 10
# set a factor for changing the resolution
myMultiplier = .2

# define the image
myImage = ImageObject(myImageName)

# phase 1 will enhance resolution, phase 2 will reduce
for myPhase in range(2):
    # this code runs once per phase
    # now loop through each frame
    for myFrameNumber in range(myFrameCount):
        # this code runs once per frame per phase
        # create a new page at the dimensions of the image
        newPage(*myImage.size())
        # get the dimensions of each cell
        myCellWidth, myCellHeight = width()/myXCount, height()/myYCount
        # now loop through the rows
        for myYNumber in range(myYCount):
            # this code runs once per row per frame per phase
            # and loop through the columns
            for myXNumber in range(myXCount):
                # this code runs once per column per row per frame per phase
                # define the x and y coordinates of each shape
                myX = myCellWidth * myXNumber
                myY = myCellHeight * myYNumber
                # and sample the color of the pixel in the image at these coordinates
                myColor = imagePixelColor(myImage, (myX, myY))
                # now set the fill to the sampled color, unpacking r, g, b, a and feeding them to fill() separately
                fill(*myColor)
                # now draw a rectangle with that fill
                rect(myX, myY, myCellWidth, myCellHeight)
        # adjust the resolution for each frame; int() is a Python operator that lops off the decimal fraction of a floating-point number            
        myXCount = int(myXCount + myXCount*myMultiplier)
        myYCount = int(myYCount + myYCount*myMultiplier) 
    
    # if we are at the end of the first phase, draw an extra frame where we see the full-res image
    if myPhase == 0:
        newPage(*myImage.size())
        # we'll pause on it for one second
        frameDuration(1)
        image(myImage, (0, 0))
    # … and then, invert myMultiplier so it works on the resolution in reverse for the second phase
    myMultiplier = -myMultiplier
    
saveImage('resolution2.gif')