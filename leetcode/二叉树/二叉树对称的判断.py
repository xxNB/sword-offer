# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        s = []
        p,q=root.left, root.right
        s.append(p)
        s.append(q)
        while s:
            p =s[-1]
            s.pop()
            q=s[-1]
            s.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            s.append(p.left)
            s.append(q.right)
            s.append(p.right)
            s.append(q.left)
            