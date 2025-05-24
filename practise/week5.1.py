n=int(input("Enter any value"))
reverse=0
while n>0:
    rem=n%10
    print(rem,end=" ")
    reverse=reverse*10+rem
    print(reverse)
    n=n//10
print(reverse)
    
