ncp1 = (75, 350)
ncp2 = (900, 375)
fcp1 = (250, 700)
fcp2 = (700, 800)
cir = 10
wid = 2.5
fSize = 25
Variable([dict(name="Position", ui="Slider", args=dict(minValue=0, value=.5, maxValue=1))], globals())
pos = Position

txt = 'Curve position: %s' %round(pos, 3)
l = FormattedString()
l.append(txt, font='LucidaGrande', fontSize=fSize, fill=(0))
text(l, (700, 50))

def lerp(c1, c2, ratio):
    return c1 + (c2 - c1) * ratio   
def lerpPt(pt1, pt2, ratio):
    return (lerp(pt1[0], pt2[0], ratio), lerp(pt1[1], pt2[1], ratio))
def circle(pt, color):
    with savedState():
        fill(None)
        stroke(*color)
        oval(pt[0] - cir/2, pt[1] - cir/2, cir, cir)
def square(pt, color):
    with savedState():
        fill(None)
        stroke(*color)
        rect(pt[0] - cir/2, pt[1] - cir/2, cir, cir)
def tri(pt, color):
    with savedState():
        fill(None)
        stroke(*color)
        s = cir
        h = s * sqrt(3)/2
        polygon((pt[0] - s/2, pt[1] - h/3), (pt[0], pt[1] + h/3 * 2), (pt[0] + s/2, pt[1] - h/3), close=True)

path = BezierPath()
path.moveTo(ncp1)
path.curveTo(fcp1, fcp2, ncp2)
fill(None)
stroke(0, .25)
strokeWidth(wid)
drawPath(path)
square(ncp1, (0, .25))
square(ncp2, (0, .25))
stroke(.75, 0, 0, .5)
line(ncp1, fcp1)
line(ncp2, fcp2)
circle(fcp1, (.75, 0, 0, .5))
circle(fcp2, (.75, 0, 0, .5))
stroke(0, .75, 0, .5)
cbp1 = lerpPt(ncp1, fcp1, pos)
cbp2 = lerpPt(fcp1, fcp2, pos)
cbp3 = lerpPt(fcp2, ncp2, pos)
polygon(cbp1, cbp2, cbp3, close=False)
tri(cbp1, (0, .75, 0, .5))
tri(cbp2, (0, .75, 0, .5))
tri(cbp3, (0, .75, 0, .5))
stroke(0, .75, 0, .25)
line(fcp1, fcp2)
stroke(0, 0, .75, .5)
cp1 = lerpPt(cbp1, cbp2, pos)
cp2 = lerpPt(cbp2, cbp3, pos)
line(cp1, cp2)
tri(cp1, (0, 0, .75, .5))
tri(cp2, (0, 0, .75, .5))
c1 = lerpPt(cp1, cp2, pos)
tri(c1, (0, 0, .75, .5))
