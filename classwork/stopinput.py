

lnum=0
while True:
    num = input("ednetr a value")
    if(num=="STOP"):
        break
    if(int(num)>lnum):
        lnum=int(num)
print("Largest number is ",lnum)

row=int(input("Enetr row"))





for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for k in range(2*row-1-2*i,0,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")



