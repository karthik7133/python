

for i in range(1,6):
    if i==3:
        break
    print("Hi")



row=int(input("Enter row"))
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")

for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\r")
