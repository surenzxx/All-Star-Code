from Myro import *
#Surendra Persaud
ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)

pic = makePicture("wacka.jpg")
pixelList = getPixels(pic)

for i in pixelList:
    pixel = i
    grayVal = getGray(pixel)
    if grayVal > 180:
        setColor(i, ObamaYellow)
    elif grayVal > 120:
        setColor(i, ObamaBlue)
    elif grayVal > 60:
        setColor(i, ObamaRed)
    elif grayVal < 60:
        setColor(i, ObamaDarkBlue)
    
show(pic)

