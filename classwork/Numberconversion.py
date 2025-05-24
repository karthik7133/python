num=int(input("Enter the value for num"))
num1=num2=num
digsum=0
B_num=0
i=0
while num2!=0:
    B_num=(B_num)+(num2%2)*(10**i)
    num2=num2//2
    i=i+1
print("Binary of the number is: ",B_num)

D_num=0
i=0
while B_num!=0:
    D_num=(D_num)+(B_num%10)*(2**i)
    B_num=B_num//10
    i=i+1
print("Binary of the number is: ",D_num)

O_num=0
i=0
while D_num!=0:
    O_num=(O_num)+(D_num%8)*(10**i)
    D_num=D_num//8
    i=i+1
print("Octal of the number is: ",O_num)

D_num=0
i=0
while O_num!=0:
    D_num=(D_num)+(O_num%10)*(8**i)
    O_num=O_num//10
    i=i+1
print("Decimal of the number is: ",D_num)

H_num=""
while D_num!=0:
    rem=(D_num%16)
    if rem<10:
        H_num= str(rem)+(H_num)
    else:
        H_num= chr(rem+ord("A")-10)+(H_num)
    D_num=D_num//16
print("Hexa of the number is: ",H_num)


