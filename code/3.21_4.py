# -*- coding: utf-8 -*-

# 输入一个链表，反转链表后，输出链表的所有元素。 ⭐️⭐️⭐️

class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        last = None

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last
