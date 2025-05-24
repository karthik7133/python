



row=int(input("Enter the value for row"))


for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=row-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\r")




for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print("\r")




for i in range(1,row+1):
    for j in range(1,i+1):
        print(i+1-j,end=" ")
    print("\n")

for i in range(1,row+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")        

k="A"
for i in range(1,row+1):
    for j in range(1,i+1):
        #print(chr(ord(k)+i-1),end=" ")
        print(k,end=" ")
        k=chr(ord(k)+1)
    print("\r")




for i in range(1,row+1):
    for j in range(row+1-i,0,-1):
        print("*",end=" ")
    print("\n")



for i in range(1,row+1):
    for j in range(row,i-1,-1):
        print("*",end=" ")
    print("\n")



for i in range(1,row+1):
    for j in range(1,row+2-i):
        print("*",end=" ")
    print("\n")

i=1
while i<=row:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+1
    print("\n")
    



k=2*row-3
for i in range(1,row+1):
    c=1
    for j in range(1,i+1):
        print("*",end=" ")
        c=c+1
    for j in range(1,k+1):
         print(" ",end=" ")
         c=c+1
    for j in range(c,2*row):
        print("*",end=" ")
        c=c+1
    k=k-2
    print("\n")




for i in range(1,row+1):
    for j in range(1,2*row):
        if (j>i and j<(2*row-i)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")            





for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")   

    print("\n")



for i in range(1,row+1):
    for j in range(1,2*row):
        if (j>i and j<(2*row-i)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")            


  







k="A"
for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(ord(k)+i-1),end=" ")
    #k=chr(ord(k)+1)
    print("\r")




k="A"
i=1
while i<=row:
    j=1
    while j<=i:
        print(chr(ord(k)+i-1),end=" ")
        j=j+1
    i=i+1
    print("\r")
    


for i in range(1,row+1):
    k="A"
    for j in range(1,i+1):
        print(k,end=" ")
        k=chr(ord(k)+1)
    print("\r")


k="A"
for i in range(1,row+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k=chr(ord(k)+1)
    print("\r")



for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")



for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=5-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\r")


k=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print("\r")

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")

for i in range(1,row+1):
    for j in range(row,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\r")

for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=(row-i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\r")



for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")
