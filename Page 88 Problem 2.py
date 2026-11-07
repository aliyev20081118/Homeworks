v1=int(input("enter volume of first object: "))
v2=int(input("enter volume of second object: "))
m1=int(input("enter mass of first object: "))
m2=int(input("enter mass of second object: "))
ro1=m1/v1
ro2=m2/v2
if ro1>ro2:
    print("density of first object")
else:
    print("density of second object")