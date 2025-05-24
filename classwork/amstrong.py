

num=int(input("Enetr a number to check amstrong"))
digit=0
sum=0
num1=num2=num3=num
while num1!=0:
    digit=digit+1
    num1=num1//10
while num!=0:
    sum=sum+((num%10)**digit)
    num=num//10
if(sum==num2):
    print("Amstrong")
else:
    print("Not an amstrong")


while num3>9:
    sum=0
    while num3!=0:
        sum=sum+(num3%10)
        num3=num3//10
    num3=sum
if(num3==1):
    print("Magic number")
else:
    print("NOt a magic number")
