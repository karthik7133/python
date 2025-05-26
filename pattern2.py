def printli(i):
    l=[]
    for j in range(8-i):
        print(" ", end="")
    for j in range(i+1):
        l.append(j)
    for k in l[1:]:
        print(k,end=" ")
def rec(i,j):
    if i==j:
        return
    else:
        printli(i)
        print()
        return rec(i+1,j)
rec(1,8)

