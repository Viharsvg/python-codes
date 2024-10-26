#handsome number examples: 123,224,235 etc.here 123 is number because last digit=3and remaining left part
# is 12 and sum of 1+2 is 3 i.e. 123-->1+2 =3 which is last digit. similarly , 347 is handsome becuase 3+4=7 islast

number=int(input("enter number:="))
last_digit=number%10
left_part=number//10
left_part_sum=0
while left_part:
    left_part_sum+=left_part%10
    left_part=left_part//10
if left_part_sum==last_digit:
    print(number," is HANDSOME NUMBER.")
else:
    print(number,"is NOT HANSOME NUMBER.")
