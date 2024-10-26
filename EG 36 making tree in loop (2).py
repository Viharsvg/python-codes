no=int(input("enter the value of no:="))
for i in range (0,no):
    for s in range(0,no-i-1):
        print(end=" ")
    for j in range(0,i+1):
         print("*",end=" ")
    print()
    
for i in range (0,no):
        print("  *****  ")
