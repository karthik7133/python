num=int(input("Enetr value for num"))
sum=sum1=0
num1=num2=num3=num
while 1:
    if num==0:
        break
    sum=sum+((num%10)**3)
    num=num//10
if sum==num1:
    print("Yes")
else:
    print("No")
        
while num2!=0:
    sum1=sum1+((num2%10)**3)
    num2=num2//10
if sum1==num3:
    print("Yes")
else:
    print("No")
        
      
