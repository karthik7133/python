#Finding even and odd numbers:
'''
Num=int(input("Enter number:"))
if Num%2==0:
    print("Given number is even")
else:print("Given number is odd")
'''
#Diff b/w num and 17:
'''
Num= int(input("Enter number:"))
if Num<=17:
  print(17-Num)
else: print(Num-17)*2       
'''
#Number is in b/w 100 or 1000 or 2000:
'''
n=int(input("enter n value"))
def near_thousand(n):
     return ((abs(1000-n)<=100)or (abs(2000-n)<=100))
print(near_thousand(n))
print(near_thousand(100))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
'''
#sum of given 3 numbers:
'''
a=int(input("enter number1:"))
b=int(input("enter number2:"))
c=int(input("enter number3:"))
sum=a+b+c
if a==b==c:
    print (sum*3)
else:print(a+b+c)
'''
'''#5
n=int(input("enter number:"))
if n<0:
    print(0)
elif n==0 or n==1:
    print(1)
else:
    fact=1
    while(n>1):
        fact*=n
        n=n-1
        print(fact)
        '''
'''#checking big number:
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:print(c)'''
#finding leep year or not:
n=int(input("enter year"))
if n%4==0:
    print("Leep year")
else: print("non leep year")    









