# create your first (sort of) animation!
# we're going to do this using a 'nested for-loop'
# first create a string variable
myString = 'the quick brown fox'

# range() is a Python function that takes one or two integer values as arguments: one argument will be interpreted as the number n of integers in a sequence, and the code will assume 0 as the starting integer in that sequence; two arguments will be interpreted as the starting integer and number n of integers respectively
# range() returns a sequence of n integers starting at the beginning integer
# list() is a Python function that transforms a sequence into a list (we'll talk about lists in class)
print(list(range(10)))
# note that the list stops at 9, which is the tenth integer if we start counting at 0
# also note that this is how computers count by default: starting at 0
# now let's use range() in a for-loop to make frames in an animation
for myPage in range(10):
    # myPage will be the number of the current page we're using as a frame; again, it will start at 0 and end at 9
    # print the current page number
    print(myPage)
    # make a new page; DrawBot has a number of predefined sizes, among them standard imperial and ISO paper formats
    newPage('Letter')
    # set the frame rate for the animation
    # frameDuration() is a DrawBot function that records for the current canvas how long it will last as a frame in a motion graphic file
    # it takes a single argument, a fraction of a second; 1 = 1 frame per second, 1/12 = 12 frames per second, etc
    frameDuration(1/12)
    # draw a rectangle the full size of the canvas
    # remember that 0, 0 by default is the bottom left corner of the canvas
    # remember that width() and height() are DrawBot functions that give us the dimensions of the current canvas
    # and remember that the default fill() color in DrawBot is black (0)
    rect(0, 0, width(), height())
    # set the font size for the letters we're going to draw
    fontSize(130)
    # now, with this canvas, we'll loop through each letter in our string and draw it on the canvas, like we did in the previous sketch
    for myLetter in myString:
        # define two variables for random horizontal and vertical positions on the canvas, like we did in the previous sketch
        myX = randint(0, width())
        myY = randint(0, height())        
        # define a random r, g, b fill color like we did in the last sketch
        fill(random(), random(), random())        
        # draw our text on the canvas at the random x, y coordinates
        text(myLetter, (myX, myY))
        # this code will run over and over until there are no more letters left in the string to loop through
    # then after exiting the string loop, the code will check to see if there are any numbers left in the range loop, meaning in this case any more frames left to draw for the animation we're making
    
# congratulations, you've just run your first nested for-loop!

# save the pages as frames in an animated .gif
# saveImage() is a Python function that saves pages in DrawBot's memory as 2d files in the file formats it supports
# it takes at least one argument, a string that names the file; the file extension in the name tells DrawBot what file format to use
# if we just supply the filename as below, DrawBot will save the file in the same folder as the location of the Python script that generates it
saveImage('myImage.gif')
# open the .gif file and view your animation!
# also, once you've run the code, you can scroll through the canvas window to see all the pages = frames in your animation