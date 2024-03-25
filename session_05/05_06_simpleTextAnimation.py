myFrameCount = 10
fontPath ='/Users/david/Dropbox/Public/Python-for-Visual-Designers-Fall-2023/session-5/code/CondorVariable-VF.ttf'

font(fontPath)
myAxisValue = listFontVariations()['wght']['minValue']
myIncrement = 50

for myFrame in range(myFrameCount):
    newPage()
    font(fontPath, 500)
    fontVariations(wght=myAxisValue)
    text('hi', (width()/2, 370), align='center')
    myAxisValue += 50
    
saveImage('hi.gif')