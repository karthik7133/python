n=int(input("Enter row value:"))
sum=0
l=[]
d=0
for i in range(n):
    sum+=i+1
print(sum)
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
        global l
        l=l+[n]
for k in range (2,1000):
    if len(l)==sum:
        break
    prime(k)
print(l,len(l))
for u in range(0,len(l)):
    if l[u]//10==0:
        l[u]=str(l[u])
        l[u]="  "+l[u]
    elif l[u]//100==0:
        l[u]=str(l[u])
        l[u]=" "+l[u]

for m in range(n):
    for o in range(n):    
        if o>n-2-m:
            print(l[d],end=" ")
            d += 1
        else:
            print(" ",end="   ")
    print()

