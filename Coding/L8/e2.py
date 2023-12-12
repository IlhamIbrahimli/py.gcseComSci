import math

def area(r):
    rSqr = r**2
    return rSqr * math.pi

def circumference(r):
    d = r*2
    return d * math.pi


print(area(5))
print(circumference(5))