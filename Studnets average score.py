a=""
total=0
b=0
dictionary={}
while a!="quit":
    name_of_student=str(input("Enter student's name: "))
    score=int(input("Enter score of subject: "))
    dictionary[name_of_student]=score
    a=str(input("If you continue, skip otherwise write 'quit': "))
    total+=score
    b+=1
    
print(dictionary)
total1=total/b
total1=round(total1, 2)
print("Average score of subject:",total1)

