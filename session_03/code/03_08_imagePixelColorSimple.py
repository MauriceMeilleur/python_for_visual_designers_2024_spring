# create a variable for the filename
myImageName = 'Juvenile_Ragdoll.jpg'
# load the image but don’t draw it to canvas
myImage = ImageObject(myImageName)

# make a new page the size of the canvas
newPage(*myImage.size())
# draw the image to the canvas
image(myImage, (0, 0))

# use the DrawBot function imagePixelColor to sample the image at a specific coordinate and get the color of the pixel at that coordinate
# the function takes the imageObject and the (x, y) coordinates
print(imagePixelColor(myImage, (500, 500)))

# set the fill color: unpack the r, g, b, a elements from the tuple returned by imagePixelColor and pass them to the fill() call separately
fill(*imagePixelColor(myImage, (500, 500)))
stroke(1)
strokeWidth(10)
# draw a rectangle so we can see the color at (500, 500)—it should be blue (unless you change the coordinates!)
rect(100, 100, 200, 200)
