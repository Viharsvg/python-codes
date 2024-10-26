#python program to find the sum of a series 1/1!+2/2!+3/3!+4/4!+........n/n!

n=int(input("enter any no:="))   #n=5
res=0
fact=1
for i in range(1,n+1):     #start=1,end=5
    fact=fact*i
    res=res+(i/fact)
print("sum of series is :=",res)

