# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        min_val = float("-inf")
        q = [(root,min_val)]
        while q:
            crr, min_val = q.pop(0)
            if crr.val >= min_val:
                ans += 1
                
            if crr.left is not None:
                q.append((crr.left,max(crr.val,min_val)))
            if crr.right is not None:
                q.append((crr.right,max(crr.val,min_val)))
        
        return ans

        