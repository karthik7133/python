a=[5,4,43,23,64]
odd=0
even=0
for k in range(0,len(a)) :
    if a[k]%2==0:
        even=even+a[k]
    else:
        odd=odd+a[k]
print("even num sum=",even)
print("odd num sum=",odd)
        
