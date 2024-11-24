class doubleLinkedList:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = doubleLinkedList(0, 0)
        self.tail = doubleLinkedList(0, 0)

        self.head.next = self.tail
        self.tail.pre = self.head

        self.capacity = capacity
        self.size = 0

        self.dic = {}  # key: node

    def remove(self, node):

        node.pre.next = node.next
        node.next.pre = node.pre
        del self.dic[node.key]
        self.size -= 1

    def append(self, node):

        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
        node.next = self.tail

        self.dic[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:

        if key not in self.dic:
            return -1
        else:
            # move the node to the tail of the list
            node = self.dic[key]
            self.remove(node)
            self.append(node)

            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)

        else:
            node = doubleLinkedList(key, value)

        if self.size >= self.capacity:
            # remove the head of the list
            self.remove(self.head.next)

        # add/move the node to the tail of the list
        self.append(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)