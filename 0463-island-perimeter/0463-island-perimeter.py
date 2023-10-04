class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0:
                    if j-1 >= 0:
                        if grid[i][j] ==1 and grid[i][j-1] == 0:
                            res += 4
                        if grid[i][j] ==1 and grid[i][j-1] == 1:
                            res += 2
                    else:
                        if grid[i][j] ==1:
                            res += 4
                else:
                    if j-1 >= 0:
                        if grid[i][j] ==1 and grid[i][j-1] == 0:
                            res += 4
                        if grid[i][j] ==1 and grid[i][j-1] == 1:
                            res += 2
                        if grid[i][j] ==1 and grid[i-1][j] == 1:
                            res -= 2
                    else:
                        if grid[i][j] ==1:
                            res += 4
                        if grid[i][j] ==1 and grid[i-1][j] == 1:
                            res -= 2
                print(res,i,j)
        return res
                


                

        