# -*- coding: utf-8 -*-

class Solution:
    def ReverseList(self, pHead):

        if not pHead or not pHead.next:
            return pHead

        last = None

        while pHead:
            # tmp用来存储下一个，作为下次循环的pHead
            tmp = pHead.next
            # last用来倒置， 上一个是下一个的next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last