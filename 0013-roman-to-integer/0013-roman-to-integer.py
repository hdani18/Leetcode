class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dic1 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        i=0
        sum = 0
        val =0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i] == 'I' and s[i+1] == 'V':
                sum += 4
                i +=2
            elif i+1 < len(s) and s[i] == 'I' and s[i+1] == 'X':
                sum += 9
                i +=2
            elif i+1 < len(s) and s[i] == 'X' and s[i+1] == 'L':
                sum += 40
                i +=2
            elif i+1 < len(s) and s[i] == 'X' and s[i+1] == 'C':
                sum += 90
                i +=2
            elif i+1 < len(s) and s[i] == 'C' and s[i+1] == 'D':
                sum += 400
                i +=2
            elif i+1 < len(s) and s[i] == 'C' and s[i+1] == 'M':
                sum += 900
                i +=2
            else:
                val += dic[s[i]]
                i += 1
        return sum+val
                        
                    
        