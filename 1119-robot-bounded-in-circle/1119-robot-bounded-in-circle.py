class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirx, diry = 0,1 #as it points in north direction
        start0 , start1 = 0,0

        for i in instructions:
            if i == "G":
                start0 += dirx
                start1 += diry
            elif i == "L":
                dirx, diry = -1*diry, dirx
            else:
                dirx, diry = diry, -1*dirx
        return ((start0,start1) == (0,0)) or ((dirx,diry) != (0,1))
        