str = "This is VIT-AP University"
count=1
for i in str:
    if i=="s":
        count=count+1
print(count)







num = 236
a = 1
while num!=0:
    d = num%10
    if d%2==0:
        a *= d
    else:
        a //=d
    num //= 10
print(a)












a,b = 2,3
a += 5
b -= a
c = a*b
if (a>b) and (b<c):
    print("Delhi")
elif (a>b)and(b>c):
    print("Mumbai")
else:
    print("Kolkata")


