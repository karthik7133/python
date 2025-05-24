



num=int(input("Take number"))
revnum=0
while num!=0:
    revnum=(revnum*10)+(num%10)
    num //= 10
print("Rev = ",revnum)
print("Num = ",num)



a=int(input("Lower limit"))
b=int(input("Upper limit"))
even=[]
for i in range(a,b+1):
    if i%2!=0:
        break
    even=even+[i]
print("Even_list = ",even)





a=int(input("Lower limit"))
b=int(input("Upper limit"))
even=[]
odd=[]
for i in range(a,b+1):
    if i%2==0:
        even=even+[i]
    else:
        odd=odd + [i]
print("Even_list = ",even)
print("Odd_list = ",odd)
    




num=int(input("Take number"))
num1=num
digsum=0
while num!=0:
    digsum=digsum+(num%10)
    num //= 10
print("Digsum = ",digsum)
print("Num = ",num)





a=int(input("Enetr the value"))
sum=0
while a>0:
    sum=sum+a
    a=a-1
    print("a = ",a)
print("Sum = ",sum)


sum=0
while 1:
    a=int(input("Enetr the value"))
    sum=sum+a
    if(a%7==0):
        break
print("Sum = ",sum)
    
