# draw a brick wall

# define the height of the bricks
myBrickHeight = 60
# and define their width to be 3x wider then their height
myBrickWidth = 3 * myBrickHeight
# there's mortar, too!
myMortarThickness = 3

# caculate how many bricks to draw to fill the canvas
# divide canvas height by brick height, rounding up
myRows = ceil(height()/myBrickHeight)
# divide canvas width by brick width, again rounding up
myCols = ceil(width()/myBrickWidth) + 1

# set the stroke width and the fill color (for the mortar)
strokeWidth(myMortarThickness)
stroke(.8, .8, .6)

# loop through the calculated range of rows
for i in range(myRows):
    # save and move out of the current state of the canvas
    with savedState():
        translate(0, i * myBrickHeight)
        # if it’s an odd-numbered row, shift one half-brick to the left
        if i % 2:
            translate(-myBrickWidth/2)
        # loop through the calculated range of columns
        for j in range(myCols):
            # save and move out of the current state of the canvas again
            with savedState():
                translate(j * myBrickWidth, 0)
                # set the fill color, so that it’s a 50/50 chance of getting a lighter or darker red
                if random() < .5:
                    fill(.5, 0, 0)
                else:
                    fill(.6, 0, 0)
                # draw the rectangle/brick
                rect(0, 0, myBrickWidth, myBrickHeight)

saveImage('bricks.png')