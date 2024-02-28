# let's loop through a sequence, doing something with each item in a sequence one at a time
# this is called a 'for-loop' and it's an important tool in coding

# create a variable called myString
myString = 'Hello world!'

# loop through each character in the string
# myLetter is a variable we create that will be equal to the current item in the sequence
# this is a temporary variable—we can call it anything as long as it's not a protected (already-used) name in DrawBot or Python, good practice is to call it something meaningful in context
for myLetter in myString:   
    # print each character (element) in the string, one at a time
    # all code that is indented will run once for each item in the sequence being looped through
    # in a string, a space is also a character, just like in a font 
    print(myLetter)
    # when there are no more items in what's being looped through, the code will exit the loop

# the following code—notice it's dedented, outside and after the loop—will only be run once
print('done!')