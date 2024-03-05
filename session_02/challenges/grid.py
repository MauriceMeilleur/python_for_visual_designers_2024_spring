# make a grid using translate() and savedState()

# define the number of columns and rows to draw
myCols = 10
myRows = 10

# determine the width and height of each column based on the size of the canvas and the number of rows/cols
myColWidth = width()/myCols
myRowHeight = height()/myCols

# draw a background, a rectangle that fills the canvas
rect(0, 0, width(), height())

# now loop through the number of rows
for myRow in range(myRows):
    with savedState():
        translate(0, myRow * myRowHeight)
        # now loop through the columns
        for myCol in range(myCols):
            with savedState():
                translate(myCol * myColWidth, 0)
                # set a random fill color
                fill(random(), random(), random())
                # now draw a rectangle or oval by essentially flipping a coin
                if random() < .5:
                    rect(0, 0, myColWidth, myRowHeight)
                else:
                    oval(0, 0, myColWidth, myRowHeight)
saveImage('grid.png')