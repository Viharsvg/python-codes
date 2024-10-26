maths=int(input("enter the value of maths:="))
sci=int(input("enter the value of sci:="))
accounts=int(input("enter the value of accounts:="))
eng=int(input("enter the value of eng:="))
cs=int(input("enter the value of cs:="))
total=maths+sci+accounts+eng+cs
print("addition of maths",maths,"and sci",sci,"and accounts",accounts,"and eng",eng,"and cs",cs," is:=",total)
percentage=total/500*100
print("percetage of maths",maths,"and sci",sci,"and accounts",accounts,"and eng",eng,"and cs",cs," is:=",percentage)
if(percentage>=90):
    print("A grade")
elif(percentage>=70 and percentage<=90):
    print("B Grade")
elif(percentage>=50 and percentage<=70):
    print("C Grade")
elif(percentage>=35 and percentage<=50):
    print("D Grade")
else:
    print("congratulations you are fail")
    
