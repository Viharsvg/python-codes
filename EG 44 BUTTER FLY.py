#BOW TIE
n=int(input("enter any no.:="))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    for s in range(1,i+1):
        if s<1:
            print(end=((2*n)-2*i)*'')
            for j in range(1,i+1):
                print('*',end='')
                print()
                for i in range (n-1,0,-1):
                    for j in range (1,i+1):
                        print('*',end='')
                        for s in range(1,i+1):
                            if s<=1:
                                print(end=((2*n)-2*i)*'')
                                for j in range(1,i+1):
                                    print('*',end='')
                                    print()
