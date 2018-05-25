#########################################################
# lru缓存策略
#########################################################

class LinkNode:
    def __init__(self, key, val, pre_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev = pre_node
        self.next = next_node


class DoubleLinkList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, node):
        """
        append a node to the double link list last
        """
        if self.size == self.capacity:
            raise ValueError("double link list has been full")
        self.size += 1
        if self.head is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def delete(self, node):
        """
         delete a node in double link list. switch(node):
           1.node == self.head
           2.node == self.tail
           3.node in the double link list middle
        """
        if self.size == 0:
            raise ValueError("can not delete empty double link list")
        self.size -= 1

        if node == self.head:
            if node.next:
                node.next.prev = None
            self.head = node.next
        elif node == self.tail:
            if node.prev:
                node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return node


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.cache_look_up = {}
        self.cache_list = DoubleLinkList(capacity)

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.cache_look_up:
            return -1
        node = self.cache_look_up[key]
        self.cache_list.delete(node)
        self.cache_list.append(node)
        return node.val

    def set(self, key, value):
        # write your code here
        if key in self.cache_look_up:
            node = self.cache_look_up[key]
            node.val = value
            self.cache_list.delete(node)
            self.cache_list.append(node)
        else:
            if self.capacity == self.cache_list.size:
                head_node = self.cache_list.delete(self.cache_list.head)
                del self.cache_look_up[head_node.key]
            new_node = LinkNode(key, value)
            self.cache_look_up[key] = new_node
            self.cache_list.append(new_node)