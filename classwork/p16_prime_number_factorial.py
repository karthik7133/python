


num=int(input("Enter the value for number"))
i=2
flag=0
while i<num:
    if num%i==0:
        flag=1
        print(num, "is  divisible by ",i)
        break
    i=i+1
if flag==0:
    print("prime number")
else:
    print("Not aprime number")


flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if flag==0:
    print("prime number")
else:
    print("Not aprime number")


fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

fact=1
for i in range(num,0,-1):
    fact=fact*i
print(fact)





    
