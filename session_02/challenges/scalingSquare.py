# make a growing square in black and white
# define the initial size of the square; this variable will grow for each frame as the code draws them
myShapeSize = 100
# how many frames should the square grow for
myFramesPerPhase = 18

# define a foreground and background color
# these will flip at the end of the first phase
fgColor = (1, 1, 1)
bgColor = (0, 0, 0)

# this animation will have two 'phases'
# the first will draw a black square, the second a white square; we can do a loop through the phases to avoid duplicating the code
for myPhase in range(2):
    # myPhase will equal first 0, then 1
    # now we'll have a nested for-loop for the frames in each phase
    for myFrame in range(myFramesPerPhase):
        # for each frame, create a new page
        newPage()
        # and set the frame duration
        frameDuration(1/15)
        # then draw the background
        fill(*bgColor)
        rect(0, 0, width(), height())
        # now shift the origin to the center
        translate(width()/2, height()/2)
        # set the foreground color and draw the rectangle
        fill(*fgColor)
        rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
        # at the end of every frame, make the square a little bigger
        myShapeSize += 50

    # at the end of the first phase, swap the foreground color the background color
    fgColor = 0, 0, 0
    bgColor = 1, 1, 1
    # and reset the shape size
    myShapeSize = 100

saveImage('scalingSquare.gif')