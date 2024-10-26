        print("="*129)
        print("WELCOME TO AREA (OPERATIONS)")
        print("="*129)
        print(" 1.area of circle \n 2.area of rectangle \n 3.area of square \n 4.area of cube")
        ch=int(input("enter your choice:="))
        if ch==1:
            print("THANKYOU \n YOU HAVE SELECTED AREA OF CIRCLE") 
            R=int(input("ente]r the value of R:="))
            pi=3.14
            print("area of circle of R:=",pi*R*R)
        elif ch==2:
             print("THANKYOU \n YOU HAVE SELECTED AREA OF RECTANGLE")
            L=int(input("enter the value of L:="))
            B=int(input("enter the value of B:="))
            H=int(input("enter the value of H:="))
            print("area of rectangle of L and B and H:=",L*B*H)
        elif ch==3:
             print("THANKYOU \n YOU HAVE SELECTED AREA OF SQUARE")
             A=int(input("enter the value of A:="))
             print("area of square of A:=",A*A)
        elif ch==4:
             print("THANKYOU \n YOU HAVE SELECTED AREA OF CUBE")
             S=int(input("enter the value of S:="))
             print("area of cube of S:=",6*S*S)
        else:
            print("OHH!NICE \n YOU HAVE ENTERED INVALID VALUE")

