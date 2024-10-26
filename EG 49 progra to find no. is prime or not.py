#program to find the no. is prime or not

n=int(input("enter the no:="))
lim=int(n/2)+1
for i in range(2,lim):
    rem=n%i
    if rem==0:
        print(n,"is not prime no")
        break
else:
    print(n,"is a prime no")
