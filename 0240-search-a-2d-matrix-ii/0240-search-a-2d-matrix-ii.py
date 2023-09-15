class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for i in range(len(matrix)):
            print(matrix[i][-1])
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                flag = True
                l,r = 0, len(matrix[i]) - 1 
            while flag and l<=r:
                mid = (l+r)//2
                if target == matrix[i][mid]:
                    return True
                if target > matrix[i][mid]:
                    l = mid+1
                else:
                    r = mid-1
            flag = False

        return False
                
