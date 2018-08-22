# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre= None

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur, m = 0, 1
        res = []
        self.dfs(root, res, m , cur)
        return res

    def dfs(self, node, res, m, cur):
        """
        :param node: 节点
        :param res: 结果
        :param m: 当前最大频次
        :param cur: 当前频次
        :return:
        """
        if not node:
            return
        self.dfs(node.left, res, m, cur)
        if self.pre and node.val == self.pre.val:
            cur+=1
        else:
            cur=1
        if cur == m:
            res.append(node.val)
        if cur>m:
            m = cur
            res = []
            res.append(node.val)
        self.pre = node
        self.dfs(node.right, res, m, cur)