help(openTypeFeatures)
print(listOpenTypeFeatures('Minion Pro'))
# make a margin
myMargin = 50

# open a text file and use its content as the value of a variable myText
with open('book.txt', encoding='utf-8') as myFile:
    # read the file into our myText variable
    myText = myFile.read()

# create a formatted string
myString = FormattedString(
    myText, 
    font='Minion Pro', 
    fontSize=40, 
    lineHeight=70, 
    tracking=0, 
    fill=(1, 0, 0),
    # activate OpenType features using a Python dictionary object, signified by curly brackets {}, in which we 'map' one value to another with a colon :
    openTypeFeatures={'smcp': True, 'onum': True}
)

# draw the bounds of our text box as a rectangle so we can see them
rect(
    myMargin, # x
    myMargin, # y
    width()-myMargin*2, # width, account for both margins
    height()-myMargin*2 # height, account for both margins
)
# draw the text box to canvas
textBox(
    myString, 
    (
        myMargin, 
        myMargin, 
        width()-myMargin*2, 
        height()-myMargin*2
    )
)