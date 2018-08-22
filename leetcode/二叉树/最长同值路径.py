class Solution:
    """
    和二叉树直径类似
    """
    res = 0
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        # res = 0
        self.helper(root)
        return self.res

    def helper(self, root_child):
        if not root_child:
            return 0
        left = self.helper(root_child.left)
        right = self.helper(root_child.right)
        left = left+1 if root_child.left and root_child.val == root_child.left.val else 0
        right = right+1 if root_child.right and root_child.val == root_child.right.val else 0
        self.res = max(self.res, left+right)
        return max(left, right)
