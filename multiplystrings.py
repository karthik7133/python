c="karthi is good boy"
k=c.split(" ")
m=""
for i in k:
    m+=i
print(len(m))
flag=True
for j in range(0,len(m)):
    b=len(m)-j
    if( m[j]!=m[b-1]) :
        flag=False
print(flag)