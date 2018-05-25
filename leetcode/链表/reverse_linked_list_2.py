
#########################################################
# 反转链表 ||
#########################################################

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        new_head = prev
        prev = new_head.next
        cur = prev.next
        for i in range(m, n):
            prev.next = cur.next
            cur.next = new_head.next
            new_head.next = cur
            cur = prev.next
        return dummy.next
