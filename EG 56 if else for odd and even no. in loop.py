print("1.programm to get even no.\n2.programm to get the odd no.")
ch=int(input("enter the choice:="))
if ch==1:
       no=int(input("enter the no:="))
       total=0
       for i in range(no):
           if i%2==0:
               total +=i
       print("the total is",total)
        
elif ch==2:
       sum=0
       no=int(input("enter any no:="))
       for i in range (1,no+1,2):
            sum=sum+i
       print("sum of ODD natural no. is:=",sum)


