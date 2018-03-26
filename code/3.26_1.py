# -*- coding: utf-8 -*-

# 给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

class Solution:
    def KthNode(self, pRoot, k):
        # 遍历顺序为左根右
        global result
        result = []
        self.midnode(pRoot)
        if k<= 0 or len(result) < k:
            return None
        else:
            return result[k-1]

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)
        