


n=int(input("Enter center value"))
for i in range(1,2*n):
    for j in range(1,2*n):
        if((i<=n)and((j<n+1-i)or(j>=n+i))):
            print(" ",end=" ")
        elif((i>n)and((j<=i-n)or(j>=3*n-i))):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")
