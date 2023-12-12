import math

def area(r):
    rSqr = r**2
    return rSqr * math.PI

def circumference(r):
    d = r*2
    return d * math.PI


print(area(5))
print(circumference(5))