class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
      
        stack = []
        for i in s:
            if stack and stack[-1][0] ==i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])

            if stack[-1][1] == k:
                stack.pop()
        print(stack)  
        ans = ""
        for i in stack:
            ans += (i[0]*i[1])  
        return ans         