#########################################################
# 反转链表
#########################################################
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        last = None
        while head.next:
            temp = head.next
            head.next = last
            head = temp
            last = head
        return head