s="anagram"
sub="nagram"
index=s.find("nagram")
print(index)
k=s[index:]
print(k)
if k==sub:
    print("true")
else:
    print("false")

