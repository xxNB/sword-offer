# -*- coding:utf-8-*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.check(root, 0, sum)

    def check(self, t, sum, a):

        if not t and sum == a:
            return True
        if not t:
            return False
        if t.left == None and t.right != None:
            return self.check(t.right, sum + t.val, a)
        if t.left != None and t.right == None:
            return self.check(t.left, sum + t.val, a)
        return self.check(t.left, sum + t.val, a) or self.check(t.right, sum + t.vla, a)
