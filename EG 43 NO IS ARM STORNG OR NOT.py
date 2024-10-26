num = int(input("Enter a number: "))
sum =0
temp = num
while (num > 0):
   sum= sum+(num % 10)*(num % 10)*(num % 10)
   num=num//10
if temp==sum:
   print(sum,"is an Armstrong number")
else:
   print(sum,"is not an Armstrong number")
