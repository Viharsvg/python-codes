print("-"*129)
print("THIS IS EMMPLOYEE PERSONAL DETAILS")
print("-"*129)
employeeno=int(input("enter the no. of your choice:="))
employeename=input("enter the name of employee:=")
basicsalary=int(input("enter the salary:="))
sa=int(input("enter the employee sales  amount:="))
if sa>=100000:
    comm=sa*0.20
elif sa>=70000 and sa<100000:
    comm=sa*0.15
elif sa>=50000 and sa<70000:
    comm=sa*0.10
elif sa<50000:
    comm=sa*0.05
else:
    print("Invalid value")
print("Commision is:=",comm)
netsalary=sa+comm
print("netsalary:=",netsalary)
