maths=int(input("enter the value of maths:="))
sci=int(input("enter the value of sci:="))
accounts=int(input("enter the value of accounts:="))
eng=int(input("enter the value of eng:="))
cs=int(input("enter the value of cs:="))
total=maths+sci+accounts+eng+cs
print("addition of maths",maths,"and sci",sci,"and accounts",accounts,"and eng",eng,"and cs",cs," is:=",total)
ans2=total/5*100
print("percentage of maths",maths,"and sci",sci,"and accounts",accounts,"and eng",eng,"and cs",cs," is:=",ans2)
if ans2>33:
    print("balak is passed")
else:
    print ("balak is failed")

