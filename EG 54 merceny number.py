#programm to find mersenne number
#mersenne number is 2pow1-1, 2pow2-1,2pow3-1=7...
#python program to print first 10 mersenne numbers

no=int(input("enter any no."))
for i in range(1,no+1):
    mersnum=2**i-1
    print(mersnum,end="")
print()
