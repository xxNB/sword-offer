# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre=0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root

    def dfs(self, root):
        if root:
            self.dfs(root.right)
            root.val = self.pre+root.val
            self.pre = root.val
            self.dfs(root.left)

