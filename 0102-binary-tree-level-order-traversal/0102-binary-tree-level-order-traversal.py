# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []  # Return an empty list if the root is None

        q = [(root, 0)]
        dic = {}
        while q:
            crr, level = q.pop(0)
            if level in dic:
                dic[level].append(crr.val)
            else:
                dic[level] = [crr.val]
            if crr.left is not None:
                q.append((crr.left, level + 1))
            if crr.right is not None:
                q.append((crr.right, level + 1))
        res = []
        for j in dic.values():
            res.append(j)
        return res










        