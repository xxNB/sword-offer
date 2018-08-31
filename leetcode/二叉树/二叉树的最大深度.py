class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        # 回溯
        rightDepth = self.maxDepth(root.right)
        return leftDepth+1 if leftDepth>rightDepth else rightDepth+1