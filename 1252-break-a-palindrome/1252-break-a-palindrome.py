class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        i =0

        while i < len(palindrome)//2:
            if palindrome[i] != "a":
                ans = palindrome[:i] + "a" + palindrome[i+1:]
                return ans
            else:
                i+=1
        
        if i == len(palindrome)//2:
            ans = palindrome[:len(palindrome)-1] + "b" 
        return ans
