#SUM OF EVEN NO'S
no=int(input("enter the no:="))
total=0
for i in range(no):
    if i%2==0:
        total +=i
        print("the total is",total)
