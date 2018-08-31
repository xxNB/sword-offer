# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head
        odd = dummy.next
        first_event = dummy.next.next
        event = dummy.next.next
        while odd and event and event.next:
            temp = odd.next.next
            odd.next  = odd.next.next
            odd = temp
            temp1 = event.next.next
            event.next = event.next.next
            event = temp1
        # odd.next = event
        # while event and event.next and event.next.next:
            # temp = event.next.next
            # event.next = event.next.next
            # event = temp
        odd.next = first_event
        return dummy.next