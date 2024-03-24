myShapeCount = 50
myShapeSize = 20
myFrameCount = myShapeCount

myMinValue = listFontVariations('CondorVariable-VF.ttf')['wght']['minValue']
myMaxValue = listFontVariations('CondorVariable-VF.ttf')['wght']['maxValue']
myItalMinValue = listFontVariations('CondorVariable-VF.ttf')['ital']['minValue']
myItalMaxValue = listFontVariations('CondorVariable-VF.ttf')['ital']['maxValue']
myValueRange = myMaxValue - myMinValue

for myFrameNumber in range(myFrameCount):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    frameDuration(1/24)
    translate(0, height()/2)  
    font('CondorVariable-VF.ttf')
    fontSize(800)
    for myShapeNumber in range(myShapeCount):
        if myShapeNumber == myFrameNumber:
            myProgress = myShapeNumber/myShapeCount
            myCurvature = sin(2*pi*myProgress)
            myItalCurvature = cos(4*pi*myProgress)
            myWaveSize = height()/2
            # remap() is a DrawBot function that takes a number that varies in one range and finds its equivalent number in a different range; in this case myCurvature and myItalicCurvature as calculated above will vary from -1 to 1 (because sine and cosine vary from -1 to 1), but we want to translate that variation into the range of weights and italic-ness in Condor
            # remap() takes a mandatory five arguments: the value to be translated, the original minimum and maximum values of the range for the value to be translated, and the new minimum and maximum values
            myWeightValue = remap(myCurvature, -1, 1, myMinValue, myMaxValue)
            myItalicValue = remap(myItalCurvature, -1, 1, myItalMinValue, myItalMaxValue)
            print(myWeightValue)
            # here we'll use our re-mapped values to adjust the weight and italic-ness of Condor for this frame
            fontVariations(wght=myWeightValue, ital=myItalicValue)
            text('Hello', (width()/2, -230), align="center")
            # to help you see the relationship between the sine function and how we're using it to vary things in our animation
            myX = myShapeNumber*myShapeSize
            myY = myCurvature*myWaveSize
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('moveAcrossPage.gif')