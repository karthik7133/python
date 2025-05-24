count_alpha=count_num=0
while 1:
    a=input("Enter for a")
    if a.isspace():
        break
    elif a.isalpha():
        count_alpha=count_alpha+1
    else:
        count_num+=1
print(count_alpha,count_num)
    
