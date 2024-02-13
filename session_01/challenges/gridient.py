# make a gradient grid by manipulating red, green, blue values
# DJR made up the name for this sketch, so if you don't like puns, groan at him, not me :)

newPage(1000, 1000)

# instead of looping through a string, the code will loop through a range of numbers
rows = 10
cols = 10

# define the size of the squares in the grid
gridSize = 100

# define starting x and y positions for the process of drawing the grid
startX = 0
startY = 0
# and define (starting) values for red, green, and blue
startR = 0
startG = 0
startB = 0
# now execute the grid loop
for row in range(rows):
    # define the y position for the row
    y = startY + row * gridSize
    # define the blue for the row; each row will get a little more blue
    b = startB + row * .1
    for col in range(cols):
        # define the x position for the column
        x = startX + col * gridSize
        # define the red for each column; each column will get a little more red
        r = startR + col * 0.1
        # set the fill color each time a square in the grid gets drawn, using the current red and blue values; the green value will stay at its starting value defined above
        fill(r, startG, b)
        rect(x, y, gridSize, gridSize)
    
saveImage('gridient.png')
