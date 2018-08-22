# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        二叉搜索树的裁剪，从根节点开始，若根节点在裁剪范围左侧，那么他和他的左子树完全裁剪；若根节点在裁剪范围右侧，那么他和他的右子树完全裁剪
        ；若根节点在裁剪范围（不用裁剪），按照递归分别推出他左右子树的裁剪结果
        """
        if root is None:
            return None
        if root.val <L:
            return self.trimBST(root.right ,L ,R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
        return root