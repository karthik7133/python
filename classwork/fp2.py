file1=open("txtf2.txt","w")
#list1 = ["Hello", "World","Hi"]
#str2 = file1.writelines(list1)
file1.write("Hi This is my class. This is my laptop")
file1.close()
file2 = open("txtf2.txt","r")
str = file2.read();
str2 = str.split();
count =0
print(str2)
for i in str2:
    if i=="This":
        count += 1
    else:
        continue
print(count)
vcount = 0;
ccount=0;

for i in str:
    if i in "UaeiouAEIO":
        vcount += 1;
    else:
        ccount += 1;
print(vcount,ccount);


