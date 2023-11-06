# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = [(root,0)]
        ans =[]
        dic ={}
        while q:
            crr,level = q.pop(0)
            if level not in dic:
                dic[level] = [crr.val]
            else:
                dic[level].append(crr.val)

            if crr.left is not None:
                q.append((crr.left,level+1))
            if crr.right is not None:
                q.append((crr.right,level+1))
        
        for val in dic.values():
            ans.append(val[-1])
        return ans