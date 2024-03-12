# create a low-res vector interpretation of an image

# variable for the filename
myImageName = 'Juvenile_Ragdoll.jpg'
# make an image object
myImage = ImageObject(myImageName)
# create a new page the size of the image but don’t draw the image
newPage(*myImage.size())

# make a grid
myXCount, myYCount = 28, 25
# calculate the cell dimensions based on canvas size and row/col count
myCellWidth, myCellHeight = width()/myXCount, height()/myYCount

# loop through each row
for myYNumber in range(myYCount):
    # loop through each column
    for myXNumber in range(myXCount):
        # get our x and y values by multiplying the column/row number by the cell size
        myX = myCellWidth * myXNumber
        myY = myCellHeight * myYNumber
        # now sample the color of the pixel in the image at (x, y)
        myColor = imagePixelColor(myImage, (myX, myY))
        # and set the fill color to that color, unpacking the r, g, b, a values and feeding them to fill()
        fill(*myColor)
        # draw an oval
        oval(myX, myY, myCellWidth, myCellHeight)