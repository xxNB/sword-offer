class Solution:
    def sumNumbers(self,root):
        return self.dfs(root,0)

    def dfs(self, root,sum):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return sum*10+root.val
        return self.dfs(root.left, sum*10+root.val)+self.dfs(root.right, sum*10+root.val)