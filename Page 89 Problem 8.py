a=float(input("Enter amount of a: "))
b=float(input("Enter amount of b: "))
c=float(input("Enter amount of c: "))
d=float(input("Enter amount of d: "))
if (a<=c and b<=d) or (a<=d and b<=c):
    print('Yes')
else:
    print('No')