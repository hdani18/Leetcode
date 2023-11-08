class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for i in range(max(len(s),len(t))):
            if i < len(s):
                if s[i] != "#":
                    stack_s.append(s[i])
                elif stack_s != []:
                    stack_s.pop(-1)
            if i < len(t):
                if t[i] != "#":
                    stack_t.append(t[i])
                elif stack_t != []:
                    stack_t.pop(-1)
        print(stack_s,stack_t)
        
        return (stack_s == stack_t) 
