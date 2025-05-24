


l=[2,3,5,8,10]
for i,j in enumerate(l):
    if(j%2==0):
        print(j,end=" ")
        print(l[i],end=" ")


l=[2,4,5,7,8,9]
for i in l:
    if(i%2==0):
        print(i,end=" ")
for i in range(len(l)):
    if(l[i]%2==0):
        print(i,end=" ")


l=[2,4,5,6]
for i in range(len(l)):
    print(l[i])

l=[2,4,5,7,8,9]
for i in l:
    if(i%2==0):
        print(i,end=" ")
for i in range(len(l)):
    if(l[i]%2==0):
        print(l[i],end=" ")







l=['a','b','c','e','h']
for i in l:
    if i not in ['a','e','i','o','u']:
    #if i in "aeiou": 
        print(i,end=" ")




l=[[2,3,4],[4,7,8,9,120]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print("\n")


l=[[2,3,5],"abcd",5,[4,6,"nmp"]]
for i in l:
    for j in list(i):
        print(j)



l=[2,3,5,8,10]
for i,j in enumerate(l):
    if(j%2==0):
        print(j,end=" ")

        
for i in range(0,len(l)):
    if(l[i]%2==0):
        print(l[i],end=" ")

        

l=['a','b','c','e','h']
for i in l:
    if i  in ['a','e','i','o','u']:
    #if i in "aeiou": 
        print(i,end=" ")



l=[[0,0,0],[0,0]]
for i in range(2):
    for j in range(len(l[i])):
        l[i][j]=int(input("Enter the value for mtrix"))
print(l)
        



a=input("Enetr anything")
