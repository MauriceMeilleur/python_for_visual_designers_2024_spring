# set the font and the font size; you can set the font to be the PostScript name of any font you have installed on your machine
font('MinionPro-Regular')
fontSize(100)

# now the code will loop through the string 'hello world'
# it'll go through each character in the string and assign it to the letter variable
# since we want more letters, we'll multiply the 'hello world' string by 10 (remember, we can do this with strings)
for letter in 'hello world' * 10:  
    # define variables to describe the x- and y-positions of the drawn letter 
    # random() yields a number between 0 and 1, so random() * width() and height() will give us random x and y coordinates between 0 and the full width/height
    x = random() * width()
    y = random() * height()
    # let's print the letter and the randomized coordinates to the console
    print(letter, x, y)
    # and we'll randomize the color of the drawn letter, because why not?
    fill(random(), random(), random())
    # and now the code will draw the letter
    text(letter, (x, y))
    
saveImage('randomly_placed_letters_loop.png')