class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s,i,j):
            while i<j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        count = 0
        for i in range(len(s)):
            count += 1
            for j in range(i+1,len(s)):
                if is_palindrome(s,i,j) == True:
                    count +=1
        return count


            

        