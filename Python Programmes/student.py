
Roll_no = int(input("enter a Roll No: "))
Name = input("enter a Name: ")
Marks = [int(input("enter a marks of subject: ")) for i in range (5)]

Total_marks = (sum (Marks))
print("Roll No: ",Roll_no)
print("Name: ",Name)

print("Subject_Marks: ",Marks)

print("total marks of studentare :",Total_marks)
Percentage = (Total_marks/500)*100
print("Percentage: ",Percentage,"%")

if(Percentage>80):
    print("grade A+")
elif(Percentage>=70 and Percentage<80):
    print("grade A")
elif(Percentage>=60 and Percentage<70):
    print("grade B+")
elif(Percentage>=50 and Percentage<60):
    print("grade C")
elif(Percentage>=40 and Percentage<50):
     print("grade D")
else:
    print("fail")






      
