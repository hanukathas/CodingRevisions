class DoubleLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:


    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLLNode(0,0)
        self.tail = DoubleLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # add node after head
    def _add_node(self, node:DoubleLLNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # remove from location
    def _remove_node(self, node: DoubleLLNode):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node: DoubleLLNode):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._move_to_head(node)
        else:
            new_node = DoubleLLNode(key=key, val=val)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove_node(self.tail.prev)
                self.cache.pop(lru.key)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    # print(cache.cache)
    print(cache.get(1))
    # print(cache.cache)# returns 1
    cache.put(3, 3)  # evicts key 2
    print(cache.cache)
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4

