a=[7,1,5,3,6,4]
a.sort()
min=min(a)
dif=0
minindex=a.index(min)
if(minindex==0):
    print(max(a)-min)

elif(minindex== len(a)-1):
    print(0)
else:
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if dif<(a[j]-a[i]):
                dif=a[j]-a[i]

    print(dif)
