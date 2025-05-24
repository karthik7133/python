





number=int(input("Enter any Number"))
print("Digit\tFrequency")
for i in range(0,10):
    count=0;
    temp=number;
    while temp!=0:
        digit=temp%10
        if digit==i:
            count=count+1
        temp=temp//10;
    if count>0:
        print(i,"\t",count)
    else:
        print(i," is not present in number")


num=int(input("Enter any Number"))
temp=num
i=0
j=0
num2=num
while(num!=0):
    digit=num%10
    temp=num2
    count=0
    while(temp!=0):
        j=temp%10
        if(j==digit):
            count+=1
        temp=temp//10
    print('no. of digits of' ,  digit, '=',count)
    num=num//10
        
n=int(input("Enter any Number"))
temp=n
i=0
k=0
j=0
l=n
flag=0
list=[]
while(n!=0):
    k=n%10
    
    #for p in range(0,len(list)):
    for p in list:
        if k==p:
            flag=1
            break
        
    if flag!=1:
        while(temp!=0):
            j=temp%10
            if(j==k):
                i+=1
            temp=temp//10
        print('no. of digits of' ,  k, '=',i)
        temp=l
        i=0
    
        n=n//10
        #list.append(k)
        list=list+[k]
    else:
        n=n//10
        flag=0
print(list)
