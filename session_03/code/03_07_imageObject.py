# create a variable for the filename
myImageName = 'black-raspberries.jpg'

# define an image object with the variable, but don’t draw it to canvas yet
myImage = ImageObject(myImageName)

# see that our image exists as an object in memory, even if we don’t see it on the canvas
print(myImage)

# print the image dimensions
print(myImage.size())

# set the canvas size to the image dimensions: use the Python operator * to unpack the width and height and pass them to newPage() as separate values
newPage(*myImage.size())

# now that the canvas is the correct size we can draw the image object to canvas
image(myImage, (0, 0))