class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # curr_sum = 0
        # max_sum = nums[0]
        
        # for i in range(len(nums)):
        #     curr_sum =0
        #     for j in range(i,len(nums)):
        #         curr_sum += nums[j]
        #         max_sum = max(curr_sum,max_sum)
                
        
        # return max_sum
        sum = 0
        max_sum = nums[0]
        for i in nums:
           
            if sum<0:
                sum =0
            
            sum +=i
            max_sum = max(sum,max_sum)
            
        return max_sum




                
                
        