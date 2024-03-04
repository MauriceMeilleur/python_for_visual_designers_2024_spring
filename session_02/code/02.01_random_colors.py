# review: animate through some colors

for myNumber in range(10):
    # print the control variable, the current number
    print(myNumber)
    # make a new page
    newPage()
    # set the fill color to random
    fill(random(), random(), random())
    # draw a rectangle starting at (0, 0) and covering the canvas
    rect(0, 0, width(), height())
# dedent so that we exit the loop
# and only save the file once
saveImage('randomColors.gif')