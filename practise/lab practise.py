'''
n=1
for i in range(6):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()

for i in range(9):
    if i>4:
        i=8-i
    for j in range(9):
        if j==4-i or j==4+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end="\n")
    
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=2
l=["H","A","R","I","S","H"]
for i in range(6):
    if i>1:
        i=5-i
    for j in range(6):
        if 2-i<=j<=3+i:
            print(l[j],end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(5):
    for j in range(4):
        if j==0 or j==3 or i==2:
            print("H",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(6):
    if i>=3:
        i=5-i
    for j in range(5):
        if j==0 or j==5-i-1:
            print("k",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(6):
    for j in range(12):
        if j>=5:
            j=11-j
        if i==j or j==0:
            print("M",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(6):
    for j in range(3):
        if i==0 or i==2 or i==4 or j+1==i:
            print("srinavas",end=" ")
        else:
            print("        ",end=" ")
    print()
l=["M","O","N","E","Y"]
for i in range(5):
    if i>2:
        i=4-i
    for j in range(6):
        if 2-i<=j<=2+i:
            print(l[j],end="  ")
        else:
            print(" ",end="  ")
    print()

for i in range(6):
    if i<2:
        for j in range(7):
            if j==4-i or j==4+i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    if i==2:
        for j in range(9):
            if j>=4+i or j<=4-i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    if i==3:
        for j in range(9):
            if j==1 or j==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    if i==4:
         for j in range(9):
            if j==2 or j==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    if i==5:
        for j in range(9):
            if 2<j<6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

k=3
for i in range(4):
    for j in range(7):
        if j>k+i or j<k-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
k=int(input("enter any  even value"))
for i in range(1,k):
    if i>k/2:
        i=k-i
    for j in range(1,k):
        if j>=(k/2)+1:
            j=k-j
        if j>i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
l=["K","A","R","T","H","I","K"]
for i in range(1,8):
    if len(l)%2!=0:
        if  i==len(l)/2+1:
            Print("*",end=" ")
        else:print(" ",end=" ")
    if i>4: 
        i=8-i
    for j in range(9):
        if 4-i<j<4+i:
            print(l[j-1],end=" ")
        else:
            print(" ",end=" ")
    print()



for i in range(7):
    for j in range(4):
        if i==0 or j==0 or j==3  or i==3 or i==6:
            print("8",end=" ")
        else:print(" ",end=" ")
    print()
n=0
for i in range(4):
    for j in range(3):
        if j==0 or i==0 or i==3:
            print("*",end=" ")
        else:print(" ",end=" ")
    if i<4:
        
        for k in range(1):
            if k==0:
                print("*",end=" ")
            else:print(" ",end=" ")
    print()
for i in range(4,7):
        for j in range(0,4):
            if j==1+n or j==0:
                print("*",end=" ")
            else:print(" ",end=" ")
        n+=1
        print()

Eg={
    "SPH01":999,
    "LAP02":1299,
    "SWT03":299,
    "TAB04":599,
    "HPH05":199,
    "BSP06":149
}
def k(a):
    return a[1]
eg=sorted(Eg.items(),key = k)
print(eg)

import numpy as np
f=1
arr = np.array([[23,22,11],[3,5,21],[17,24,20],[12,14,13]])
print(arr)
for i in range(4):
    for j in range(3):
        a=(arr[i][j])
        t=(arr[i][j])
    for k in range(2,a):
        if a%k==0:
            f=1
        else:
            t=0
            (arr[i][j])=t   
print(arr)

l=[]
SUM=0
n=1
a=float(input("Enter any value"))
k=a
r=float(input("Enter any value"))
if r>1:
    for i in range(0,5):
        digit=a*(r**i)
        l.append(digit)
        SUM+=digit
    print(l)
    print(SUM)
if r<1:
    for i in range(0,10000000):
        digit=a*(r**i)
        l.append(digit)
        SUM+=digit
    print(SUM)
'''
n=int(input("Enter any value"))
t=n
sum=0
fact=1
l=[]
if n==0:
    fact=1
while t>0:
    digit=t%10
    if digit>0:
        for j in range(1,digit+1):
            fact=fact*j
    t=t//10
    l=l+[fact]
    sum+=fact
    fact=1
print("sum =",sum)
if sum==n:
    print("Its a krishnamurthi number")


n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

        


    

        
    

    
    















    
