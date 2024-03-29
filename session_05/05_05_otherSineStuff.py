myShapeCount = 50
myShapeSize = 20
myFrameCount = 50


for myFrameNumber in range(myFrameCount):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    frameDuration(1/24)
    translate(0, height()/2)

    for myShapeNumber in range(myShapeCount):
        if myShapeNumber == myFrameNumber:
        # if True:
            myProgress = myShapeNumber / myShapeCount
            myCurvature = cos(2*pi*myProgress)
            myWaveSize = height()/2
            myY = myCurvature*myWaveSize
            myX = myShapeNumber*myShapeSize
            #myX = width()/2
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('moveAcrossPage.gif')