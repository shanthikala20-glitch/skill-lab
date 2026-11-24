marks=int(input("enter your marks"))
if marks>100 or marks<0:
    print("Invalid marks")
elif marks>=90 and marks<=100:
    print("A Grade")
elif marks>=70 and marks<=80:
    print("B Grade")
elif marks>=60 and marks<=75: 
     print("C Grade")
elif marks>=50 and marks<=65: 
    print("D Grade")     
else:
    print("pass")
    