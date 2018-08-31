# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root ==q:
            return root
        L = self.lowestCommonAncestor(root.left, p,q)
        R = self.lowestCommonAncestor(root.right, p,q)
        # 俩边能同时回溯到root，即为最近公共父节点
        if L and R:
            return root
        # 哪边回不了root 就向上回溯
        return L if L else R