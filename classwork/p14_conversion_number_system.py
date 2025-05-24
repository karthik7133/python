num=int(input("Enter the value for num"))
num1=num2=num
digsum=0
while num!=0:
    digsum=digsum+(num%10)
    num=num//10
print("Sum of the digits is: ",digsum)
    
R_num=0
while num1!=0:
    R_num=(R_num*10)+(num1%10)
    num1=num1//10
print("Reverse of the number is: ",R_num)


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

