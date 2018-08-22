
class Solution:
    def hasCycle(self,head):
        fast=slow=head
        while  fast:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                return True
        return False