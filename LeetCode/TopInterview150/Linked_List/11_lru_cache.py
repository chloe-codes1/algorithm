class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node: ListNode) -> None:
        prev_tail = self.tail.prev
        prev_tail.next = node

        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self._remove(node)
        self._add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)

        node = ListNode(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            
            del self.cache[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
