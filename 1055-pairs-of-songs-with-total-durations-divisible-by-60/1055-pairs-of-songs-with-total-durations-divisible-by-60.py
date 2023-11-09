class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(len(time)):
        #     for j in range(i+1,len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1
        # return count
        ans = 0
        dic ={}

        for i in time:
            val = i % 60
            if val == 0:
                # ans += dic[0]
                ans += dic.get(0, 0)
            elif (60-val) in dic:
                ans += dic[60-val]
            
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
        return ans
            
