class Solution:
    def leafSimilar(self, root1, root2):
        v1,v2 = [], []
        self.dfs(root1,v1)
        self.dfs(root2,v2)
        if len(v1) != len(v2):
            return False
        for i in range(len(v1)):
            if v1[i]!=v2[i]:
                return False
        return True

    def dfs(self, root, v):
        if not root:
            return
        if root.left:
            self.dfs(root.left,v)
        if root.right:
            self.dfs(root.right,v)
        if not root.left and not root.right:
            v.append(root.val)
        return

