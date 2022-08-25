#Link - https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self,key,val) -> None:
        self.key,self.val = key,val
        self.prev,self.next = None, None

class LRUCache:
    def __init__(self,capacity) -> None:
        self.capacity  = capacity
        self.cache = {}
        #left is the least recently used and right is the most recently used
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self,node: Node):
        '''remove the node from the left side of the list (least recently used)'''
        prev,next = node.prev,node.next
        prev.next,next.prev = next,prev
    def insert(self,node: Node):
        '''Insert the node on the right side of the doubly linkedlist'''
        prev,next = self.right.prev,self.right
        prev.next=next.prev = node
        node.prev,node.next = prev,next
    
    def get(self,key):
        if key in self.cache:
            #remove the key from the list and add it to right end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self,key,val):
        if key in self.cache:
            #there is an existing key, we will remove it
            self.remove(self.cache[key])
        #update the cache and the linkedlist
        self.cache[key]= Node(key,val)
        self.insert(self.cache[key])
        if self.capacity < len(self.cache):
            #delete the lru node
            lru =  self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    