class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_ = 200
        for i in strs:
            if len(i) < min_:
                min_ = len(i)
        res = ''
        for i in range(min_):
            for j in range(len(strs)):
                temp = strs[0][i]
                if strs[j][i] != temp:
                    return res
            res += temp
        return res
            