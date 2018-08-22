# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        递归比较各个节点的左孩子和右孩子
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return True
        if abs(self.getDepth(root.left)-self.getDepth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        """
        求出节点深度
        :param root:
        :return:
        """
        if not root:
            return 0
        return 1+max(self.getDepth(root.left),self.getDepth(root.right))
