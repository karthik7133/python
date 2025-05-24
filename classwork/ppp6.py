







L=[2,4,6,1,9]
for i in range(0,len(L)):
    for j in range(i+1,len(L)):
        if L[i]>L[j]:
            continue
    


#m=int(input("Enter row size"))
#n=int(input("Enter coloumn size"))
a=[[1,2,3],[2,4,5],[4,6,7]]

for i in range(3):
    for j in range(3):
        a[i][j]=0
    print("\n")
for i in range(3):
    for j in range(3):
        a[i][j]=int(input("Enetr element"))
    print("\n")
print(a)





a=input("Enter a string")
vs=""
cs=""
for i in a:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        vs=vs+i
    else:
        cs=cs+i
print("vovel string= ",vs)
print("Cons string= ",cs)


a=input("Enter a string")
vs=""
cs=""
for i in range(0,len(a)):
    if a[i] in ['a','e','i','o','u','A','E','I','O','U']:
        vs=vs+a[i]
    else:
        cs=cs+a[i]
print("vovel string= ",vs)
print("Cons string= ",cs)
