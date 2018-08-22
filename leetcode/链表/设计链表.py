class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkList:
    def __init__(self):
        """
        initialize your data structure here
        """
        self.head = None
        self.size = 0

    def get(self, index):
        if index<0 or index >= self.size:
            return -1
        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size+=1

    def addAtTail(self, val):
        curr =self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not  None:
                curr = curr.next
            curr.next= Node(val)
        self.size+=1

    def addAtIndex(self, index, val):
        if index<0 or index>self.size:
            return
        elif index==0:
            self.addAtHead(val)
        elif index==self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(1,index):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size+=1

    def deleteAtIndex(self,index):
        if index<0or index>=self.size:
            return
        curr = self.head
        if index==0:
            self.head = curr.next
        else:
            for i in range(1,index):
                curr =curr.next
            curr.next = curr.next.next

        self.size-=1
