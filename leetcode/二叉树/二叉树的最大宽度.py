

class Solution:
    Max = -1
    count = [0 for _ in range(100)]

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 0)

    def dfs(self, root, k):
        if not root:
            return
        self.count[k] += 1
        if self.Max < self.count[k]:
            self.Max = self.count[k]
        self.dfs(root.left, k + 1)
        self.dfs(root.right, k + 1)
