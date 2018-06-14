#########################################################
# 复制带随机指针的链表
#########################################################


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


"""
总结起来，实际我们对链表进行了三次扫描，第一次扫描对每个结点进行复制，然后把复制出来的新节点接在
原结点的 next 指针上，也就是让链表变成一个重复链表，就是新旧更替；第二次扫描中我们把旧结点的随
机指针赋给新节点的随机指针，因为新结点都跟在旧结点的下一个，所以赋值比较简单，就是 node->next
->random = node->random->next，其中 node->next 就是新结点，因为第一次扫描我们就是把新结
点接在旧结点后面。现在我们把结点的随机指针都接好了，最后一次扫描我们把链表拆成两个，第一个还原
原链表，而第二个就是我们要求的复制链表。因为现在链表是旧新更替，只要把每隔两个结点分别相连，
对链表进行分割即可。
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        curr = head
        # step1: generate new List with node
        while curr is not None:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next

        # step2: copy random pointer
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # step3: split original and new List
        newHead = head.next
        curr = head
        while curr is not None:
            # 赋值
            newNode = curr.next
            # 指向
            curr.next = curr.next.next
            if newNode.next is not None:
                newNode.next = newNode.next.next
            # 此时的curr.next已经是curr.next.next.next了
            curr = curr.next

        return newHead
