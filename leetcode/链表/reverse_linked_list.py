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
       prev = None
       curr = head
       while curr:
           nextTemp = curr.next
           curr.next = prev
           prev = curr
           curr = nextTemp
       return prev