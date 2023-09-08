class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        def compare(a,b):
            if a == '(' and b != ')':
                return False
            if a =='{' and b!= '}':
                return False
            if a =='[' and b!= ']':
                return False
            
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i]) 
            else:
               
                if len(stack) == 0 :
                    return False 
                if (compare(stack[-1],s[i])) != False:
                    stack.pop()
                else:
                    return False
                
        if len(stack) !=0:
            return False
        
        return True
            
            