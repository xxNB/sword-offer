class Solution:
    """
    和二叉树直径类似
    在递归函数中，我们首先对其左右子结点调用递归函数，得到其左右子树的最大相同值路径，下面就要来看当前结点和其左右子结点之间的关系了，如果其
    左子结点存在且和当前节点值相同，则left自增1，否则left重置0；同理，如果其右子结点存在且和当前节点值相同，则right自增1，否则right重置0。
    然后用left+right来更新结果res。<而调用当前节点值的函数只能返回left和right中的较大值>，因为如果还要跟父节点组path，就只能在左右子节点中
    选一条path，当然选值大的那个了
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
        left = left + 1 if root_child.left and root_child.val == root_child.left.val else 0
        right = right + 1 if root_child.right and root_child.val == root_child.right.val else 0
        self.res = max(self.res, left + right)
        return max(left, right)
