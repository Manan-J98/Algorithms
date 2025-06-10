class Node:
    def __init__(self, key=0, val = 0):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node  
        
    def removeAtFront(self):
        if self.head.next == self.tail:
            return None
        lru = self.head.next
        self.remove(lru)
        return lru

    
    def remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(self.cache[key])
            self.q.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.q.remove(node)
            node.val = value
            self.q.insert(node)
        elif len(self.cache) == self.capacity:
            node  = self.q.removeAtFront()
            del self.cache[node.key]
            newNode = Node(key, value)
            self.q.insert(newNode)
            self.cache[key] = newNode
        else:
            node = Node(key, value)
            self.q.insert(node)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)