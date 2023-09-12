class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # lst_s = []
        # lst_t = []
        # count_s = 1
        # count_t = 1
        # for i in range(len(s)):
        #     if i != len(s)-1 and s[i] == s[i+1]:
        #         count_s += 1
        #     else:
        #         lst_s.append(count_s)
        #         count_s = 1
        #     if i != len(t)-1 and t[i] == t[i+1]:
        #         count_t += 1
        #     else:
        #         lst_t.append(count_t)
        #         count_t = 1

        # return lst_s == lst_t
        dic_s,dic_t ={},{}
        for i in range(len(s)):
            # s[i], t[i]
            if (s[i] in dic_s.keys() and dic_s[s[i]] != t[i]) or (t[i] in dic_t.keys() and dic_t[t[i]] != s[i]):
                return False
            dic_s[s[i]] = t[i]
            dic_t[t[i]] = s[i]
        return True
        print(dic_s,dic_t)
