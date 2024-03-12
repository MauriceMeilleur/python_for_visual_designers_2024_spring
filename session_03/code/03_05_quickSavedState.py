# savedState() review

# set the fill color to red
fill(1, 0, 0)
oval(0, 0, 100, 100)

# create a saved state—all canvas formatting in this indented block will revert once we exit the block
with savedState():
    # set the fill color to green
    fill(0, 1, 0)
    # set a rotate and skew, and draw a shape
    rotate(20)
    skew(50)
    rect(200, 200, 100, 100)

# dedenting returns us to the previous state of the canvas, where the fill color is red
fontSize(100)
text('hello world', (500, 500))