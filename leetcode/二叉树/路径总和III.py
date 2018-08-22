class Solution:
    def pathSum(self, root, sum):
        res = 0
        if not root:
            return res
        return self.dfs(root, sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)

    def dfs(self, root, sum):
        res = 0
        if not root:
            return res
        if root.val == sum:
            res+=1
        res+=self.dfs(root.left,sum-root.val)
        res+=self.dfs(root.right, sum-root.val)
        return res
