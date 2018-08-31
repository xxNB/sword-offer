# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        中序遍历的逆过程,左根右
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.sorted_child(head, None)

    def sorted_child(self, head, tail):
        if head==tail:
            return None
        if head.next == tail:
            root = TreeNode(head.val)
            return root
        mid, temp = head, head
        while temp!=tail and temp.next !=tail:
            mid = mid.next
            temp = temp.next.next
        root = TreeNode(mid.val)
        root.left = self.sorted_child(head, mid)
        # 回溯
        root.right = self.sorted_child(mid.next, tail)
        return root


