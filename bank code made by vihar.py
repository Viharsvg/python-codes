def login():
    uname1 = input("Enter your username : ")
    pswd1 = input("Enter your pswd : ")
    if uname==uname1 and pswd==pswd1 :
        return True
    elif uname!=uname1 or pswd!=pswd1:
        return False
def deposit():

    
    if login()==True:
        global balance
        amount=int(input("Enter the amount to deposit :"))
        balance = balance+amount
def withdraw():
    if login()==True:
        global balance      
        amount1=int(input("Enter the amount to withdraw :"))    
        if(balance-amount1>=10000):
            balance=balance-amount1
        else:
            print("Transaction can't be completed")
def CheckBalance():
    if login()==True:
        print("Your Balance is : ",balance)
def logout():
    print("Loged out of account successful")
print("**Welcome to Royal Children Bank**")
uname = input("Set your username : ")
pswd = input("Set password : ")
balance = 25000
while True:
    print("1--deposit")
    print("2--withdraw")
    print("3--check balance")
    print("4--log out")
    ch=int(input("Enter your choice : "))
    if ch==1 :
        deposit()
    elif ch==2 :
        withdraw()
    elif ch==3 :
        CheckBalance()
    elif ch==4 :
        logout()
        quit()
