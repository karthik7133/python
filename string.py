s="hi my name is karthik"
k=""
l=s.split(" ")
print(len(l[-1]))
i=0
while(s[i-1]!=(" " or ',')):
    k+=s[i]
    i-=1
print(len(k))