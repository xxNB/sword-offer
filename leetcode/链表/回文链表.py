# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        time O(n)
        space O(1)
        """
        if head == None and head.next == None:
            return True
        slow=fast=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        first = slow
        cur = first.next
        pre = None
        while cur !=None:
            first.next = pre
            pre = first
            first = cur
            cur = cur.next
        first.next = pre
        while first !=None and head!=None:
            if first.val !=head.val:
                return False
            first = first.next
            head = head.next
        return True



