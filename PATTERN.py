def assigner(m,l,pos):
    for i in range(4):
        for j in range(4):
            if (i + j == pos) and (m[i][j]==0):
                m[i][j] = l
                l += 1
    return l
matrix = [[0] * 4 for i in range(4)]
l=1
for pos in range (7):
    result =assigner(matrix,l,pos)
    l=result
for i in matrix:
    print(i)