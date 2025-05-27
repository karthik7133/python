n1=[1,2]
n2=[3,4]
n1=n1+n2
n1.sort()
print(n1)
d=(int)((len(n1)-1)/2)

print(d)
if (len(n1) % 2 == 0):
    c = (n1[d] + (n1[d+1]))
    c /= 2

else:
    c = n1[d]
print(c)
