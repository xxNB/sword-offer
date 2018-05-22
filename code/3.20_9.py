# -*- coding: utf-8 -*-

# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, exceptNumber):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == exceptNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, exceptNumber - root.val)
        right = self.FindPath(root.right, exceptNumber - root.val)
        for i in left + right:
            res.append([root.val] + i)
        return res
        