# number of segments to draw for the polygon
mySegmentCount = 100
# create an empty list, we'll add points to it
myPointList = []

# loop through the range of segments
for mySegmentNumber in range(mySegmentCount):
    # get random coordinates for x, y
    myX = randint(0, width())
    myY = randint(0, height())
    # and append them as a tuple to the list
    myPointList.append((myX, myY))
    # print as we go to watch the list grow
    print(myPointList)

# make the stroke red
stroke(1, 0, 0)
# and set no fill
fill(None)
# now draw the polygon; use * to unpack the list of (x, y) coordinate tuples to feed them to polygon() separately
polygon(*myPointList)