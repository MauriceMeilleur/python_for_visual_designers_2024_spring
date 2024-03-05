# set the number of frames
myFrames = 5
# and the size of the circles
myShapeSize = width()*2

# for-loop through each frame
for myFrame in range(myFrames):
    # draw a new page
    newPage()
    translate(width()/2, height()/2)
    for myShape in range(50):        
        if myShape % 2:
            fill(random(), random(), random())
        else:
            fill(1)
        oval(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
        scale(.9)
        
saveImage('concentricShapes.gif')