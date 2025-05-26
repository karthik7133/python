def row(m, i):
    return m[i]

def column(m, i):
    col = [row[i] for row in m]
    return col
def revlist(l):
    j=[]
    for i in range(len(l) - 1, -1, -1):
        j.append(l[i])
    return j
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
l=[]
k=[]
h=[]
for i in range(4):
    R=row(matrix, i)
    h+=R[i:4-i]
    C=column(matrix,3-i)
    h+=C[i+1:4-i]
    l=row(matrix,3-i)
    r=revlist(l)
    h+=r[i+1:4-i]
    k=column(matrix, i)
    c=revlist(k)
    h+=c[1:4-i-1]
print(h[:-1])