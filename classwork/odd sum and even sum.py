n=int(input("Enter any value="))
even=1
odd=1
for k in range(1,n):
    if k%2==0:
        even=even*k
    else:odd=odd*k
print("even multiple=",even)
print("odd  multiple=",odd)
