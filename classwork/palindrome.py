def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1
print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))




def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")



def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
 
 
s = "chandan"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))
