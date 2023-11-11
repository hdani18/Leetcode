class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        for i, j in items:
            if i in dic:
                dic[i].append(j)
            else:
                dic[i] = [j]
        ans = []
        for key, value in dic.items():
            value.sort(reverse=True)
            avg = int(round(sum(value[:5])/min(len(value),5)))
            ans.append([key,avg])
        return ans

        