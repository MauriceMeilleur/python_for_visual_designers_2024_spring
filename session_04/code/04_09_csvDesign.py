# this script adjusts positions by eye, but you could also set them relative to each other as variables

# import the csv library
import csv
# define an inch as 72 points
myInch = 72.0

# open our csv file and assign it to a variable myFile
with open('fantasy_conference.csv', encoding='utf-8') as myFile:
    # read myFile with the csv reader and make it the value of myCSV
    myCSV = csv.reader(myFile)
    # loop through each row in the .csv
    for myRow in myCSV:
        # unpack each row into variables for each column
        myName, myCompany, myRole = myRow
        print(myName)
        # make a new page, business card size
        newPage(3.5 * myInch, 2 * myInch)
        # set the font and OpenType features
        font('Minion Pro', 18)
        openTypeFeatures(smcp=True)
        # draw a text box for the name
        # define the right side of the box relative to the canvas width
        #rect(20, 70, width()-110, 50)
        textBox(myName, (20, 70, width()-110, 50))
        # draw the affiliation in red in the bottom left
        fill(1, 0, 0)
        # turn off the smcp feature
        openTypeFeatures(smcp=False)
        # adjust the font size
        fontSize(12)
        # draw the affiliation text
        text(myCompany, (20, 30))
        # scale the canvas in order to scale the logo image (it's large and surrounded by a bunch of space)
        scale(0.4)
        # draw the logo by pointing the code to the source of an image online, feature of the DrawBot image() functionality
        image('https://universityinnovation.org/images/5/5c/Cooper_union_logo.png', (420, 130))
        