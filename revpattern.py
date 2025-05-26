for i in range (4):
    for j in range (7):
        if(i==0):
            print("* ",end="")
        elif(i>0):
            if(j==i or j==6-i):
                print("* ",end="")
            else:
                print("  ",end="")
    print()