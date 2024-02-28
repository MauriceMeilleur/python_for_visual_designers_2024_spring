# split is a Python function for strings
ourNames = """Jaamal
Mia
Jocelyn
Amy
Jerel
Nick
Marisa
Maurice
Ayat""".split('\n')

# shuffle is a function from the ramdom module installed with DrawBot
shuffle(ourNames)
for aName in ourNames:
    print(aName)