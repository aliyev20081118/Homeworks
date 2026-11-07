import math
s1=int(input("enter amount of area for square: "))
s2=int(input("enter amount of area for circle: "))
a=math.sqrt(s1)
r=math.sqrt(s2/math.pi)
dc=2*r
ds=a*math.sqrt(2)
if dc>ds:
    print("Area of square is in the area of circle")
else:
    print("Area of circle is not in the area of square")
