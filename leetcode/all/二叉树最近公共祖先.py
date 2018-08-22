
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return None

        if root == p or root ==q:
            return root

        # 递归
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
