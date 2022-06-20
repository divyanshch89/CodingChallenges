"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#LC Link - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#This is the approach 1
#Complexity:
#TC - Linear
#SC - Linear
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q  = [root]
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                #only point to the next node when the current is not the last node in the current level
                if i<size-1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

#approach 2 is more intuitive and do not use the stack to keep track of the nodes on a particular level
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#Complexity:
#TC - Linear
#SC - Constant
class Solution:
    def processChild(self,childNode,prev,leftMost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                #first node of the next level
                leftMost = childNode
            prev = childNode
        return prev,leftMost
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        leftMost = root
        while leftMost:
            prev,curr = None,leftMost
            leftMost = None
            while curr:
                prev,leftMost = self.processChild(curr.left,prev,leftMost)
                prev,leftMost = self.processChild(curr.right,prev,leftMost)
                curr = curr.next
        return root
        

        