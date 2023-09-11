class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        temp =[]
        for i in range(len(strs)):
           temp.append (''.join(sorted(strs[i])))
        print(temp)
        for i in range(len(temp)):
            if temp[i] is None:
                continue
            ans =[strs[i]]
            for j in range(i+1, len(temp)):
                if temp[i] == temp[j]:
                    ans.append(strs[j])
                    temp[j] = None
            res.append(ans)
        return res
                