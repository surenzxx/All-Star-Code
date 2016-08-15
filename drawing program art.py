from Processing import *
from random import *
#Surendra Persaud
window(1000, 1000)

def draw():
    random1 = randrange(0,255)
    random2 = randrange(0,255)
    random3 = randrange(0,255)
    randomx = randrange(0,200)
    randomy = randrange(0,200)
    fill(random1, random2, random3)
    rect(mouseX(), mouseY(), randomx, randomy)

framerate=(500)
onLoop+= draw
loop()