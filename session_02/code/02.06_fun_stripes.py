# use a for-loop to draw five frames
for myFrame in range(5):
    # for each frame, create a new page
    newPage()
    # (re)set the x value to 0
    myX = 0
    # a nested for-loop to loop through 10 numbers
    for myNumber in range(10):
        # draw a rectangle 50 units wide and the full height of the canvas
        # the x position will be the myX variable
        fill(random(), random(), random())
        rect(myX, 0, 50, height())
        # increase myX by 100 to it every pass through this loop; the drawn rectangles will shift to the right each pass
        myX += 100
    # here the code exits the stripe loop
    
# here the code exits the frame loop
# and now we can save the animation
saveImage('funStripes.gif')