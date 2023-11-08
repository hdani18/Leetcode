class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        stack = []
        for i in s:
            if i != ")" :
                stack.append(i)
            else:
                while stack:
                    val = stack.pop()
                    if val != "(":
                        ans.append(val)
                    else:
                        break
                for i in ans:
                    stack.append(i)
                ans =[]

        return "".join(stack)