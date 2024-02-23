class LRUCache:
    class Node:
        def __init__(self, key, val, next, prev):
            self.key, self.val = key, val
            self.prev, self.next = prev, next

    def __init__(self, capacity: int):
        self.hm = {}
        self.maxCap = capacity
        self.lru = LRUCache.Node(0, 0, None, None)
        self.mru = LRUCache.Node(0, 0, None, None)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    # L - LRU
    # R - MRU
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        curKey = self.hm[key]        
        self.delete(curKey)
        self.insert(curKey)
        return self.hm[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.delete(self.hm[key])

        self.hm[key] = LRUCache.Node(key, value, None, None)
        self.insert(self.hm[key])

        if len(self.hm) > self.maxCap:
            curLRU = self.lru.next
            self.delete(curLRU)
            self.hm.pop(curLRU.key)
