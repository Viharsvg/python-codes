#pythonprogram to check given np. is perfect number or not
#note;a perfect number is a positive integer which  is equal to sum of its divisor eg no 28 (1+3+4+7+14=28)
n=int(input("enter the no:="))
sum=0
for i in range (1,n):
    if(n%i==0):
        sum=sum+i
if (sum==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")


