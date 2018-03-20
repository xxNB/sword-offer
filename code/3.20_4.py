# -*- coding: utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        p = RandomListNode(pHead.label)
        p.next = pHead.next
        p.random = pHead.random

        p.next = self.Clone(pHead.next)
        # 返回复杂链表的head
        return p


