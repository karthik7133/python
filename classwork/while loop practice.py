x=int(input("Enter any value="))
k=1
even=1
odd=1
while k<x:
    if k%2==0:
        even=even*k
    else: odd=odd*k
    k=k+1
print("even sum=",even,"odd sum=",odd)
