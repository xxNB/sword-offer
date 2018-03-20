# -*- coding: utf-8 -*-


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