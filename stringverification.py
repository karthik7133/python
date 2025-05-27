s=['[','{','(']
g="]})"
g1="[]{}()"
c=0
flag=False
for i in g1:
        if(i in s):
            c=g.find(i)
            if(i in g):
                d=g.find(i)
                if c<d:
                    flag=True
                else:break

print(flag)

