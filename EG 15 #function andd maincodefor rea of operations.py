#function
def line():
    print("="*117)
def star():
    print("*"*117)
def AOC():
    print("THANKYOU \n YOU HAVE SELECTED AREA OF CIRCLE") 
    R=int(input("enter the value of R:="))
    pi=3.14
    print("area of circle of R:=",pi*R*R)
def AOR():
    print("THANKYOU \n YOU HAVE SELECTED AREA OF RECTANGLE")
    L=int(input("enter the value of L:="))
    B=int(input("enter the value of B:="))
    print("area of rectangle of L and B:=",L*B)
def AOS():
    print("THANKYOU \n YOU HAVE SELECTED AREA OF SQUARE")
    A=int(input("enter the value of A:="))
    print("area of square of A:=",A*A)
def AOCUBE():
    print("THANKYOU \n YOU HAVE SELECTED AREA OF CUBE")
    S=int(input("enter the value of S:="))
    print("area of cube of S:=",6*S*S)
    print("="*117)
def ND():
    print("OHH!NICE \n YOU HAVE ENTERED INVALID VALUE")
#maincode
print("WELCOME TO AREA (OPERATIONS)")
line()
star()
print(" 1.area of circle \n 2.area of rectangle \n 3.area of square \n 4.area of cube")
ch=int(input("Enter Your Choice:="))
if ch==1:
    AOC()
elif ch==2:
    AOR()
elif ch==3: 
    AOS() 
elif ch==4:
    AOCUBE()
else:
    print("YOU HAVE SELECTED WRONG VALUE")
