# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

    def merge(self, h1, h2):
        """归并排序"""
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return dummy.next

    def sorList(self, head):
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            # 按中间划开
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        # 从小merge到大
        return slow.merge(self.sorList(head), self.sorList(slow))