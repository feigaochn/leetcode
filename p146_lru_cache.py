class DoubleLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.kv = dict()
        self.count = 0
        self.head = DoubleLinkedNode(-1, -1)
        self.tail = DoubleLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self.remove(node)
        self.append(node)
        return node.value

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = node.next = None

    def append(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last
        node.next = self.tail
        self.tail.pre = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.kv:
            node = DoubleLinkedNode(key, value)
            self.count += 1
        else:
            node = self.kv[key]
            node.value = value
            self.remove(node)
        self.kv[key] = node
        self.append(node)
        while self.count > self.capacity:
            self.count -= 1
            remove = self.head.next
            self.remove(remove)
            del self.kv[remove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    cache = LRUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))  # 1
    print(cache.put(3, 3))
    print(cache.get(2))  # -1
    print(cache.put(4, 4))
    print(cache.get(1))  # -1
    print(cache.get(3))
    print(cache.get(4))
    print(cache.get(2))  # -1


def test():
    cache = LRUCache(2)
    for call, param in zip(["put", "put", "put", "put", "get", "get"],
                           [[2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]):
        print(cache.__getattribute__(call)(*param))


if __name__ == '__main__':
    # main()
    test()
