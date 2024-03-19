print(listFontVariations('/Users/meilleur/Desktop/cooper/week_04/code/CondorVariable-VF.ttf'))

# define a margin
myMargin = 50

# we can define a variable with a string we get from reading a file...
#with open('book.txt', encoding='utf-8') as myFile:
#    myText = myFile.read()

# ...or we can define the text in the code as a multiline string
myText = '''
Acerio. 9593025 Is mi, ipician dipsam experum quis plisiti atemole cepera nobit aliatqui natemque sum rest et di  235 aceperero ommoluptatet volut et, sinvelici sequiant est as sus, sum, in num id quias nossint, quis 2342 nusdae 1010101 abor sendam nis adit occae excepro dolorehenis delignihilla debit utatet et lisqui odit qui te sequi re nis maionecatqui officabore, officil iquamus audit minulpa rchiliatium, tes doluptasimet estiur aliquid magnat iniento et rectatet ersperum ea as dolut pe pa cuptat od expliquisqui bla dolesero mo blam, tentiat antotatios experia asi asperitaquam velitectota sunt et voluptas volorep taquiamus.
Aperio que poreptae ere, voluptibust, sequas aut rem. Et dolupta vit et quae sanda ipsam, vellita voluptiis alicia velitate verum ratur? Quidiste eumento es sit, ilit hilibusa cullandae nobis eatiunt lacepuda nim re dolestior aut harum quam cus dendis reribus eumquas sendios tibus.
To eliatibus et, quis qui to exeria ducid que diteni il mi, con eiunti omnihit aut ulloribus voluptur, qui acestiis doluptatio. Nam iur soluptatur?
Ribusa dolest, ommos explis resequa spidipsam quo quatemquam rem et ea nossum et aruptaturio. Aceperrovid et verrorernat utemporum sinctus restis magnieni sin nus am que quos unto consedia volupta tureritibus, sin porerum, toremporem acia voluptam, vollit volum, sint.
Molorem ut dolut eos dolorep eribusda numquat emporibus ute si debis millest entem eres sit pos que lam, optatur, sitatiat ut videst reriorepuda aceperciunto bere conecturit velenia ipidel inim facerio. Nam, solorunt ma porerumque rescid eate ni repe nient in reptate dolorrum et et fuga. Bus et ea prent eum, atatur aliquod quiatum quatem exerum aut quo inim desed es rehenec aerferunt, inis as asimi, opta cus, conse vel maximaiorem quae conet et ute del essit quatiat enimolupiet peri volorias erum haris modi conempor reratet que offic te diate nonesti ostios aut ipsuntis nimagnat ute nonecati volupit aturiam aut fugit eum fuga. Et accuptatem la dolupta tiatia venis acerum quam, consed mintia ea conseni musantis rehene labo. Et acepudae vent aut lit quas arciae pa parum hit ad mi, est, con comnihi catur?
Gendaecabore consed que nimolore voluptio volorep ernatur, odit et quia nit oditatio quo dunt, omnimeniet maximpo rporiaero beatendae ni optibuscit que nate pres sum rehenti cus.
Aquas eium rae. Et praeperio vent laborunt ium audit, odit andicatum aut fugia dolupta tiorpos dis molo cum quam aliquam, qui dolo qui doloris es acearum esequam repeles non porum saped ut est laturit praestr uptate landus, comnihi cimillor aliquos exerovide rehendam voluptatur aut ut audaepelit as eatecat emporem sam quaspel igente acepere necta ipidenist, omnimil modia vel iur, optaque dit volendi ut aperovit, quaspel itatur? Giatio occuptas provita testibus event hictur alitat ex eiume reruptinctia cullati animpos animagnam aut quiae. Fugitiis ut poratur alis seque et omnis perrum ut que volupta que res aut doluptios estia excest vid qui unt.
'''

# define a variable as a formatted string
myString = FormattedString(
    myText, # the text to draw
    font='CondorVariable-VF.ttf', # our font string can also refer to a filename (the font doesn't have to be installed on our computer)
    # other formatting
    fontSize=35, 
    lineHeight=50, 
    tracking=0, 
    fill=(1, 0, 0),
    # set the values of some variable font axes using a dictionary like we did for OpenType features, but now using fontVariations
    fontVariations={'wdth': 100, 'wght': 900, 'ital': 1},
    # set the alignment of the text in the string
    align="justified",
    )
    
# define a variable for page numbers
myPageNumber = 1

# create a while loop, a Python function that loops a bock of code as long as a specified condition is true
# we'll use a while function to draw new pages with text from the string in myString (with its formatting) as long as myString has content left in it to draw; when myString is empty, stop the loop
while myString: # means: while there is text left to draw; a string (temporary, in memory for the while loop) with characters in it has a Boolean value of True and an empty string has the value of False
    # draw a new page
    newPage()
    # draw the rectangle of our text bounds
    rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
    # draw the text box to canvas; the DrawBot function textBox will return any remaining undrawn text
    # so what we're doing with this code is (re)defining myString each time we go through the while loop
    # the amount of text left over will get less and less with each loop until the string is empty 
    myString = textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
    # draw a page number on the canvas
    fontSize(30)
    font('Georgia')
    fill(0, 1, 0)
    # convert the page number to a string with the Python operator str() in order to draw it to canvas as text
    text(str(myPageNumber), (20, 40))
    # increase the page number by 1 each time through the loop
    myPageNumber += 1