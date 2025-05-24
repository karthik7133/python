n=int(input("Enter any value"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("Its a not prime")
else:
    print("its a prime")
        
