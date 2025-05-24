'''for i in range(6):
    for k in range(5-i):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    print(end="\n")

k=0
n=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(1,7):
    for j in range(i):
        k=i+j
        k=k-i
        print(n[k],end=" ")
    print()

for i in range(1,7):
    for j in range(1,7):
        if j<=6-i:
            print(" ",end="  ")
        else:
            print("$",end="  ")
    print(end="\n")

for i in range(1,6):
    for j in range(1,6):
        if j>i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(0,5):
    for j in range(1,10):
        if j>5:
            j=10-j
        if j>5-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

c=input("Any value")
if c in "1234567890":
    print("its num")
elif "z" or "Z">c>"A" or"a":
    print("its a charecter5")

for i in range(8):
    if i>4:
        i=7-i
    for j in range(4):
        if j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        if j==3-i:
            print("*",end=" ")
        else:print(" ",end=" ")
    
for i in range(8):
     for k in range(3,0,-1):
        if k==i:
            print("*",end=" ")
        else:print(" ",end=" ")
     print()

n=int(input("Enter n value"))
i=0
while i<n:
    print(i+1)
    i+=1

k=0
l=["A","B","C","D"]
for i in range(4):
    for j in range(7):
        for k in range(j-i):
            if j>3:
                j=6-j
            if j>=3-i:
                print(l[k],end="")
            else:
                print(" ",end="")
    print()

def sum(m,n):
    p=m+n
    return p
x=int(input("Enter any value"))
y=int(input("Enter any value"))
print(sum(x,y))


def fact(n):
    f=1
    for i in range(1,n+1):
        r=f*i
        f=r
    return r
n=int(input("Enter any value which u want to find factorial"))
print(fact(n))

def prime(n):
    f=0
    if  n==1:
        print("Its neigher a prime nor a composite")
        return
    if n==0:
        print("its not a prime")
        return
    for i in range(2,n):
        if n%i!=0:
            f=1
        elif n%i==0:
            f = 0
            break
    if f==1:
        print( "Its a prime")
    else:
        print("Its not a prime")
n=int(input("Enter a number:"))
prime(n)

rev=0
n=int(input("Enter any value:"))
while n>0:
    k=n%10
    rev=10*rev+k
    n=n//10
print(rev)

def f(n):
    if n==1:
        return 1
    else:
        fact=n*f(n-1)
        return fact
n=int(input("enter any value"))
print(f(n))
'''
def rev(x):
    t=n
    if t==0:
        return rn
    else:
        rev=rev*10+rev(t%10)
        t//=10
        return rev
n=324
print(rev(n))

















































    
