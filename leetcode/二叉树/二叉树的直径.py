class Solution:
    res = 0

    def diameterOfBinaryTree(self,root):
        self.maxDepth(root)
        return self.res

    def maxDepth(self, node):
        if not node:
            return 0
        left= self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        self.res = max(self.res, left+right)
        return max(left, right)+1