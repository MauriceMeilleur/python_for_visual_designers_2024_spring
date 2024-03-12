# how many lines to draw
myLineCount = 250

# how far will we keep our lines from the edge (we could make this value negative, too)
myMargin = 50 

# round the end of each line
lineCap('round')

# set the fill color
fill(.9)
# draw our margin space once: left margin offset, bottom margin offset, width of canvas minus two margins, height of canvas minus two margins
rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)

# set the stroke width
strokeWidth(10)

# now loop through our line count
for myLineNumber in range(myLineCount):
    # set the stroke to a random color
    stroke(random(), random(), random())    
    # randomly calculate 4 coordinates, for the start (x, y) and the end (x, y)—we'll use randint() and stay inside our margin space
    myStartX = randint(myMargin, width() - myMargin)
    myStartY = randint(myMargin, height() - myMargin)
    myEndX = randint(myMargin, width() - myMargin)
    myEndY = randint(myMargin, height() - myMargin)    
    # draw the line from (x1, y1) to (x2, y2)
    line((myStartX, myStartY), (myEndX, myEndY))