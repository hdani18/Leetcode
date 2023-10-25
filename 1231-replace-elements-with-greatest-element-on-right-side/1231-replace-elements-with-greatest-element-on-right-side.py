class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res =[-1] * len(arr)
        if len(arr) >1:
            max_ = max(arr[1:])
            for i in range(len(arr)-1):
                if max_ == arr[i]:
                    max_ = max(arr[i+1:])
                res[i] = max_
            return res
        return [-1]
            
        

        
        