n=6
c=0

d=0
for i in range(1,n+1):
    if(i%3!=0):
        c+=i
    elif(i%3==0):d+=i
print(c-d)