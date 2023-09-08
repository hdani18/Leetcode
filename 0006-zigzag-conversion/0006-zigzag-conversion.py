class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None and numRows <= 0:
            return ""
        if numRows == 1:
            return s

        res = ""
        step = (numRows-1) * 2
        for i in range(numRows):
            for j in range(i, len(s), step):
                res += s[j]
                if i!= 0 and i != numRows-1 and (j+ step -2 *i) < len(s):
                    res += s[j+ step -2 *i]
                # else:
                #     res += s[i]
        return res