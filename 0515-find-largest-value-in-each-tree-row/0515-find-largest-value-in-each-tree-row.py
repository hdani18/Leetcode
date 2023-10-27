# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        dic = {}
        q = [(root,0)]

        
        while q:
            
            crr, level = q.pop(0)
           
            if level in dic:
                dic[level] = max(crr.val, dic[level])
            else:
                dic[level] = crr.val
            
            if crr.left != None:
                q.append((crr.left,level+1))
            if crr.right != None:
                q.append((crr.right,level+1))
        
        for i in dic.values():
            q.append(i)
        return q

