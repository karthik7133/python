nterms=int(input("Enter the number of terms in Fib"))
n1=0
n2=1
print(n1,end=" ")
print(n2,end=" ")
while nterms>2:
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    nterms=nterms-1
   
ntm=int(input("Enter the number of terms in Fib"))
n1=0
n2=1
print(n1)
print(n2)
for i in range(ntm-2):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
  
   
