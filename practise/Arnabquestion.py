for i in range(7):
    if i<=3:
        for j in range(4):
            if j==0 or j==3 or i==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        for j in range(4,8):
            if i==0 or i==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
for i in  range(4,7):
    for k in range(0,4):
        if i==6 or k==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(4,8):
        if k==3 or k==7 or i==3:
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
        
