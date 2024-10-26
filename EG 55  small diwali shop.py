def flowerpot():
    print("-"*117)
    pr int("1.simple flower pot\n >price=180rs\n >no.of pieces=10\n2.small matla flower pot\n >price=200rs\n >no. of pieces=8\n3.big matla flower pot\n >price=180rs \n >no.of pieces=4\n4.siren flower pot\n >price=120rs\n >no.of pieces=10\n5.sparkling flower pot\n >price=200rs\n >no.of pieces=10")
    print("-"*117)
    ch=int(input("Enter your Choice:="))
    qty=int(input("Enter the Quantity:="))
    if ch==1:
        price=180*qty  
    elif ch==2:
        price=200*qty
    elif ch==3:
        price=180*qty
    elif ch==4:
        price=120*qty
    elif ch==5:
        price=200*qty
    else:
        print("OPPS YOU HAVE ENTERD WRONG NO.")
    print("-"*117)
    return price
def bomb():
    print("-"*117)
    print("1.Mirchi bomb\n >price=80rs\n >no.of pieces=36\n2.555 bomb\n >price=100rs\n >no. of pieces=10\n3.lakshmi bomb\n >price=100rs\n >no.of pieces 10\n4.sutdi bomb\n >price=140rs\n >no.of pieces=10")
    print("-"*117)
    ch=int(input("Enter your Choice:="))
    qty=int(input("Enter the Quantity:="))
    if ch==1:
        price=80*qty  
    elif ch==2:
        price=100*qty
    elif ch==3:
        price=100*qty
    elif ch==4:
        price=140*qty
    else:
        print("OPPS YOU HAVE ENTERD WRONG NO.")
    print("-"*117)
    return price
def rocket():
    print("-"*117)
    print("1") 
    

















print("<>"*58)
print("-"*117)
print("VIHAR DHAMAKA SHOP")
print("-"*117) 
print("<>"*58)
name=input("enter your name:-")
address=input("pls enter your address:-")
print("THANKYOU FOR ENTERING YOUR DETAILS")
print("<>"*58)
print("-"*117)
print(" 1.FLOWERPOT \n 2.HAVMOR \n 3.CREAMBELL \n 4.AMUL \n 5.VIMAL \n 6.QAULITY WALLS \n 7.RAJASTHAN ICECREAM \n 8.ASHARFI KULFI \n 9.B&R")
print("<>"*58)
print("-"*117)
ch=int(input("enter your choice:="))
if ch==1:
    print("FLOWERPOT")
    price=flowerpot()
    print("<>"*58)
    print("-"*117)
    print("Your Bill")
    print("-"*117)
    print("<>"*58)
    print(" Name : ",name,"\n Address : ",address,"\n You Have selected flower pot\n Your total Amount is : ",price,"\n Thank you visit again")
elif ch==2:
    print("BOMB")
    price = bomb()
    print("<>"*58)
    print("-"*117)
    print("Your Bill")
    print("-"*117)
    print("<>"*58)
    print(" Name : ",name,"\n Address : ",address,"\n You Have selected bomb\n Your total Amount is : ",price,"\n Thank you visit again")
 
