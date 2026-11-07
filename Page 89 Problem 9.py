r=float(input("Enter amount of radius of Anar's head: "))
a=float(input('Enter amount of length for window: '))
b=float(input('Enter amount of width for window: '))
d=2*r
if d<=a and d<=b:
    print("Anar's head will fit through the window.")
else:
    print("Anar's head won't fit through the window.")
