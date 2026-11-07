a=int(input("enter amount of a for triangle: "))
b=int(input("enter amount of b for triangle: "))
c=int(input("enter amount of c for triangle: "))
if a>abs(b-c) and a<b+c and c>abs(a-b) and c<a+b and b>abs(a-c) and b<a+c:
    print('These amonuts are suitable for triangle.')
else:
    print('These amonuts are not suitable for triangle.')