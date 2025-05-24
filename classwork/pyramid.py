



c=int(input("Enter centre value"))
for i in range(1,2*c):
    for j in range(1,2*c):
        if(i<=c and ((j<=c-i)or(j>=c+i))):
            print(" ",end=" ")
        elif(i>c and ((j<=i-c)or(j>=3*c-i))):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")



for i in range(1,2*c):
    for j in range(1,2*c):
        if(i<=c and (c+1-i<=j<=c+i-1)):
            print("*",end=" ")
        elif(i>c and (i-c+1<=j<=3*c-i-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
