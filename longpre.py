strs = ["flower","flow","flight"]
c=[]
for j in range(0,len(strs)):
    c.append(len(strs[j]))
d=min(c)
print(d)
k=""
for i in range(0,d-1):
        if all(s[i] == strs[0][i] for s in strs):
            k+=strs[0][i]
        else:break

print(k)