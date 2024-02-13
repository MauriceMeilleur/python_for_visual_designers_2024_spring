# define a page with the format of a composition book
inch = 72
newPage(7.48*inch, 9.84*inch)

# define a dot radius
radius = 7.5

# draw a lot of circles
for myNumber in range(3000):
    # random() * width() is a random point between 0 and the full width of the canvas (width()).
    x = random() * width()-radius
    y = random() * height()-radius
    oval(x, y, radius * 2, radius * 2)
  
# draw a white background for a rectangle in the middle of the page
fill(1)
rect(100, 295, width()-200, 200)

# set fill to black and the font to courier
fill(0)
font('Courier New Bold')
# the font size is arbitrary; we'll save how to calculate it for later in the workshop
fontSize(20)
# draw the text with a 100pt border
text('Composition Notebook', (148, 390))

saveImage('composition_notebook.png')
