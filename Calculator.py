#Surendra Persaud
def add(x, y):
    i = 0
    while i < y:
        x = x + 1
        i = i + 1
    print (x)

def subtract(x, y):
    i = 0
    while i < y:
        x = x - 1
        i = i + 1
    print (x)
    
def multiply(x, y):
    a = 0
    while y > 0:
        for i in range (x):
            a = a + 1
        y = y - 1
    print (a)

add(x, y)
subtract(x, y)
multiply(x, y)
