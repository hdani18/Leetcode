class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i =0 
        j = len(height) -1
        while i<j:
            if height[i]> height[j]:
                area = (j-i)* height[j]
                ans = max(ans,area) 
                j-=1
            else:
                area = (j-i)* height[i]
                ans = max(ans,area)
                i+=1
            
            
        return ans
            