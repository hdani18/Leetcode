class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic ={}
        min_val = float("inf")
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i  
            else:
                dic[s[i]] = "Not"
        for j in dic.values():
            if j < min_val and j !="Not":
                min_val = j
        return min_val if min_val != float("inf") else -1


