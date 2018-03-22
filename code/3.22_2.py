# -*- coding: utf-8 -*-

# 输入一棵二叉树，判断该二叉树是否是平衡二叉树

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        lp = pRoot.left
        rp = pRoot.right
        lt = rt = 0
        while lp:
            lt += 1
            lp = lp.left
        while rp:
            rt += 1
            rp = rp.right
        if lt == rt:
            return True