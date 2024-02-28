# see how many fonts we have installed
# and see what they are

# print() is a Python function that prints to the console
# len() is a Python function gives us the length of a sequence/iterable
# installedFonts() is a DrawBot function that produces a list of all the currently-installed fonts on the machine it's run on

# print the length of the list of installed fonts
print(len(installedFonts()))

# now print the list itself
print(installedFonts())