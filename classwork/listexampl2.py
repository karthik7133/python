








def sum(a,b):
    return (a+b)
l1=[2,3,7]
l2=[4,8,1]
l3=list(map(sum,l1,l2))
print(l3)





def odd(x):
    if x%2!=0:
        return True
def mul(x):
    x=x*2
    return x



L=[1,3,4,6,7,9]
#L=list(filter(odd,range(1,21)))
L=list(filter(odd,L))
L1=list(map(mul,L))
print(L)
#print(L1)


def add(a,b):
    sum=a+b
    return sum
m=int(input("Enter first numbner"))
n=int(input("Enter second numbner"))
c=add(m,n)
print("Sum = ",c)






l1=[2,4,6]
l2=[3,5,7]
l=[0,0,0]
                                


for i in range(len(l1)):
    l[i]=l1[i]+l2[i]
print(l)













l3=[(i,j) for i in [2,3,5] for j in [3,5,7] if (i!=j)]
print(l3)
l=[]
l1=[2,3,5]
l2=[3,5,7]
for i in l1:
    for j in l2:
        if(i==j):
            continue
        l=l+[(i,j)]
print(l)

for i,j in enumerate(l):
    print(i,j)
    
L=[3,6,8,7]
for i,j in enumerate(L):
    if(L[i]%2==0):
        print(i,j)
