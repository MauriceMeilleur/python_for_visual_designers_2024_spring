# let’s make a grid!

myXCount, myYCount = 10, 10
# determine the shape width and height based on the canvas size and the number of rows and columns
myShapeWidth, myShapeHeight = width()/myXCount, height()/myYCount

# loop through our rows
for myYNumber in range(myYCount):
    # code at this indent will run 10 times, once for each myYNumber
    print('begin row number', myYNumber)
    # loop through our columns
    for myXNumber in range(myXCount):
        # code at *this* indent will run 100 times
        fill(random(), random(), random())
        # calculate our X and Y by multiplying the column/row number by the shape size
        myX = myXNumber * myShapeWidth
        myY = myYNumber * myShapeHeight
        # print our column information ('\t' is a tab character in a string)
        print('\tcol', myXNumber, myX)
        # draw our shape, an oval(x, y, width, height)
        oval(myX, myY, myShapeWidth, myShapeHeight)