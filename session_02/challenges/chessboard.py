canvas = 800
nSquares = 8
square = canvas/nSquares

newPage(canvas, canvas)
fill(1)
rect(0, 0, width(), height())
fill(0)
for i in range(nSquares):
    y = i * square
    for j in range(nSquares):
        x = j * square
        if (i + j) % 2 == 0:
            rect(x, y, square, square)
                
saveImage('chess.png')