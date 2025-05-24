def sum(y):
    s=0
    while y!=0:
        digit=y%10
        s+=digit
        y//=10
    return s





