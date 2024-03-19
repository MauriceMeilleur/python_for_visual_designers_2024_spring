# import the Python csv library
import csv
# open the .csv file as a new control variable myFile
with open('fantasy_conference.csv', encoding='utf-8') as myFile:
    # use the csv library’s reader() function to read our CSV into an interator
    myCSV = csv.reader(myFile)
    # now we can iterate through the csv row by row
    for myRow in myCSV:
        # unpack each column from the row (myRow) into variable names
        myName, myCompany, myRole = myRow
        # print(myName, '/', myCompany)
        print('%s/%s' %(myName, myCompany))