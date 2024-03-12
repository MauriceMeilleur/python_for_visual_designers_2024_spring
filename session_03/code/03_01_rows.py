# draw a row of circles

# define our x count—and our y count, for later use
myXCount, myYCount = 10, 10
# define the shape dimensions
myShapeWidth, myShapeHeight = 100, 100

# visualize the range we are looping through to draw the row
print(list(range(myXCount)))

# loop through that range of numbers
for myXNumber in range(myXCount):
    # get the x position by multiplying the column number (0–9) by the shapeWidth
    myX = myXNumber * myShapeWidth
    # print our results
    print('col', myXNumber, myX)
    # draw the shape, an oval (x, y, width, height)
    oval(myX, 0, myShapeWidth, myShapeHeight)