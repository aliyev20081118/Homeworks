import math

a=float(input("enter amount of a: "))
b=float(input("enter amount of b: "))
c=float(input("enter amount of c: "))
if a==0:
    print ('This is not a quadratic equation.')
else:
    d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("there are two real roots")
elif d==0:
    x=-b/(2*a)
    print('there is one real root')
else:
    print('There is not a real root')