s = ['[', '{', '(']
g = [']', '}', ')']
string="{}("
stack = []
flag = True
for i in string:
    if i in s:
        stack.append(i)
    elif i in g:
        if not stack:
            flag = False
            break
        expected = s[g.index(i)]
        if stack[-1] == expected:
            stack.pop()
        else:
            flag = False
            break
if stack:
    flag = False
print(flag)

