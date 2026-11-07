import math
a=int(input("enter amount of a for square: "))
r=int(input("enter amount of r for circle: "))
sq=a**2
sr= math.pi * (r ** 2)
if sq>sr:
    print("area of square")
else:
    print("area of circle")


