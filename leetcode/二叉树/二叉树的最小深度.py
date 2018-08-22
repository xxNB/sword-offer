
class Solution:

    def minDepth(self, root):
        """
        最小深度定义：从根节点到叶子结点的最短路径上的节点数
        :param root:
        :return:
        判断左子树或右子树是否为空，若左子树为空，则返回右子树的深度，反之返回左子树的深度，如果都不为空，则返回左子树和右子树深度的最小值
        """
        if root is None:
            return False
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left) +1
        # 计算左右深度
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if leftDepth<rightDepth:
            return leftDepth+1
        return rightDepth+1
