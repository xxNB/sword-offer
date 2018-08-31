# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        引入一个变量，记录该节点的左子树中节点的个数
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        cnt = self.coutNode(root.left)
        if k<=cnt:
            return self.kthSmallest(root.left,k)
        # 此处加一为根节点
        elif k>cnt+1:
            return self.kthSmallest(root.right,k-1-cnt)

        return root.val

    def coutNode(self, root):
        if root is None:
            return 0
        return self.coutNode(root.left) + self.coutNode(root.right)+1