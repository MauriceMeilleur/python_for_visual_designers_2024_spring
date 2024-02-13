newPage()

# define the number of shapes to draw
myShapeCount = 2000
# define the size of the shapes
myShapeSize = 25
# DrawBot draws from the lower left by default, so if we want the circle to be centered on the (x, y) coordinate we define, we offset it a little 
myShapeOffset = myShapeSize/2

# loop through the range between 0 and myShapeCount, creating the temporary variable myShape for each count in the process
for myShape in range(myShapeCount):
    # set fill to a random RGB color; random() yields a float between 0 and 1
    fill(random(), random(), random())
    # set the x and y variables as a random fraction of the width and height of the canvas respectively
    myX = random()*width()
    myY = random()*height()
    # draw the oval
    oval(
        myX - myShapeOffset, # x position minus offset
        myY - myShapeOffset, # y position minus offset
        myShapeSize,
        myShapeSize # setting width and height the same means the oval will be a circle
        )

saveImage('confetti.png')