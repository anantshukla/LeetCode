class Node:
    def __init__(self, key, val, next, prev):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

    
class LRUCache:
    def __init__(self, capacity: int):
        self.cacheHM = {}
        self.maxCap = capacity
        self.dummyLRU = Node(0, 0, None, None)
        self.dummyMRU = Node(0, 0, None, None)
        self.dummyLRU.next = self.dummyMRU
        self.dummyMRU.prev = self.dummyLRU
    
    # L - LRU
    # R - MRU
    def insert(self, node):
        prev, nxt = self.dummyMRU.prev, self.dummyMRU
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cacheHM:
            return -1
        node = self.cacheHM[key]        
        self.delete(node)
        self.insert(node)
        return self.cacheHM[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheHM:
            self.delete(self.cacheHM[key])

        self.cacheHM[key] = Node(key, value, None, None)
        self.insert(self.cacheHM[key])

        if len(self.cacheHM) > self.maxCap:
            lru = self.dummyLRU.next
            self.delete(lru)
            self.cacheHM.pop(lru.key)
