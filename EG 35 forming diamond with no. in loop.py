no=int(input("enter the value of no:="))
for i in range (1,no):
    for s in range(0,no-i-1):
        print(end=" ")
    for j in range(1,i+1):
         print(j,end=" ")
    print()

for i in range (no-1,0,-1):
    for s in range(0,no-i-1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
