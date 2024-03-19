# define a margin
myMargin = 50

# open a text file with the Python function open() and the control variable myFile
# define it as the variable myFile using the Python function read()
with open('book.txt', encoding='utf-8') as myFile:
    # read the file into our myText variable
    myText = myFile.read()

# define a variable as a FormattedString, and use it to formate the string in myText
myString = FormattedString(myText, font='Comic Sans MS', fontSize=40, lineHeight=70, tracking=0, fill=(1, 0, 0))

# draw a box on the canvas
rect(
    myMargin, # x
    myMargin, # y
    width() - myMargin*2, # width, account for both margins
    height() - myMargin*2 # height, account for both margins
)
# now draw a text box on the canvas with the same dimensions, and myString as its content
textBox(
    myString, 
    (
    myMargin, 
    myMargin, 
    width() - myMargin*2, 
    height() - myMargin*2
    )
)