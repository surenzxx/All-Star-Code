from Processing import *
#SURENDRA PERSAUD
window (1000, 600)
background(255,255,255)

#red
rect(0,0,100,60)
fill(255,0,0)

#green
rect(100,0,100,60)
fill(0,255,0)

#blue
rect(200,0,100,60)
fill(0,0,255)

#yellow
rect(300,0,100,60)
fill(255,255,0)

#pink
rect(400,0,100,60)
fill(255,20,147)

#turquoise
rect(500,0,100,60)
fill(0,206,209)

#orange
rect(600,0,100,60)
fill(255,165,0)

#indigo
rect(700,0,100,60)
fill(75, 0, 130)

rect(800,0,100,60)
fill(0,0,0)

rect(900,0,100,60)
fill(0,0,0)

def colorbank():
    if mouseX() <100:
        fill(255,255,255)
    elif mouseX() < 200:
        fill(255,0,0)
    elif mouseX() < 300:
        fill(0,255,0)
    elif mouseX() < 400:
        fill(0,0,255)
    elif mouseX() < 500:
        fill(255,255,0)
    elif mouseX() < 600:
        fill(255,20,147)
    elif mouseX() < 800:
        fill(0,206,209)
    elif mouseX() < 800:
        fill(255,165,0)
    elif mouseX() < 900:
        fill(75, 0, 130)
    elif mouseX() < 1000:
        fill(0,0,0)
 
def draw():
    noStroke()
    if mouseY() > 80:
        ellipse(mouseX(),mouseY(),50,50)
 
def paintBrush():
    if mouseButton() == 1:
        if mouseY() < 60:
            colorbank()
        if mouseY() > 60:
            draw()

def mousePress():  
    if mouseButton() == 1:
        print( "Mouse is pressed")
        ellipse(mouseX(),mouseY(),50,50)
        

frameRate(500)
onLoop += paintBrush
loop()

frameRate(500)
if mouseButton() ==1:
    onLoop += draw
loop()