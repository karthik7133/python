class Solution(object):
    def isValid(self, string):
        """
        :type string: str
        :rtype: bool
        """
        s = ['[', '{', '(']
        g = [']', '}', ')']
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
        return flag

