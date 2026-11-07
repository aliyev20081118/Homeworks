num=int(input("Write a three-digit number: "))
a=num//100
b=(num//10)%10
c=num%10
if a<b and b<c:
        print("The numbers are in ascending order.")
else:
    print("The numbers aren't in ascending order.")
