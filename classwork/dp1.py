def gcd(a,b):
    if (a%b==0):
        return b
    else:
        a,b=b,a%b
        return gcd(a,b)
a=int(input("Value for a"))
b=int(input("Value for b"))
g=gcd(a,b)
print(g)

def digitsum(num):
    if num==0:
        return 0
    else:
        return num%10 + digitsum(num//10)
num = int(input("Value for num"))
print(digitsum(num))
