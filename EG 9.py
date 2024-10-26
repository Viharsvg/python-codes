n1=int(input("enter the value of N1:="))
n2=int(input("enter the value of N2:="))
print("1.addition,2.subtraction,3.multiplication,4.divison,5.reminder")
ch=int(input("enter your choice:="))
if ch==1:
    print("addition on n1 and n2 is:=",n1+n2)
elif ch==2:
    print("subtraction of n1 and n2 is :=",n1-n2)
elif ch==3:
    print("multiplication of n1 and n2 is:=",n1*n2)
elif ch==4:
    print("division of n1 and n2 is:=",n1/n2)
elif ch==5:
    print("reminder of n1 and n2 is:=",n1%n2)
else:
    print("tumhare dwaraa dali gai rakam manya nhi hai krupya karke sahi likhye")
