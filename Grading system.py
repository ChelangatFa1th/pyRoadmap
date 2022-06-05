#elif statement is used for execution of more than one condition
#the execution is based on the conditions stated by the programmer
#Example is a grading system where more than pone option is involved

marks= int(input("enter the marks: "))
if (marks < 40):
    print(" E")
elif (marks >= 40 and marks < 50):
    print("D")
elif(marks >= 50 and marks < 60 ):
    print("C")
elif( marks >= 60 and marks < 70):
    print("B")
elif(marks >= 70 and marks <=100):
    print("Congratulations!, you scored an A") 
else:
    print("Invalid marks")


    