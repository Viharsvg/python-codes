#HOLOW SQuare pyramid

no=int(input("enter the no:="))
for i in range(no):
    for j in range(no):
        if i==0 or i==no-1 or j==0 or j==no-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

