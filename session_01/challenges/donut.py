# define the thickness of the donut
thickness = 300

# draw a big circle 
# use width() and height() to make the circle the full size of the new page
newPage()
fill(0)
oval(0, 0, width(), height())

# now draw a smaller white circle on top of the black circle
fill(1)
# the x and y positions of the smaller circles will be offset by the thickness value
# to calculate its width and height requires a little math
# the width will be equal to the width of the canvas/larger circle minus the thickness of *both sides* of the donut; the same respectively for height
oval(thickness, thickness, width() - thickness * 2, height() - thickness * 2)

saveImage('donut.png')