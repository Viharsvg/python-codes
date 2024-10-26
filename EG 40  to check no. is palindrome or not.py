n=int(input("enter any no:="))
num=n
rev=0
while(num>0):         
    dig=num%10        
    rev=rev*10+dig    
    num=num//10       
               
if(n==rev):           
    print(n,"IS  PALIDROME")
else:
    print(n,"IS NOT PALIDROME")


