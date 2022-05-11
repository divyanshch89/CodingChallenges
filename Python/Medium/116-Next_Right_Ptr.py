#Link - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#Recursive
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        if root.left:
            root.left.next = root.right
            self.connect(root.left)
        if root.right:
            root.right.next = root.next.left if root.next else None
            self.connect(root.right)
        return root


#Iterative approach using BFS
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        root.next = None
        q = [root]
        while q:
            current = q.pop(0)
            if current.left:
                current.left.next = current.right
                q.append(current.left)
            if current.right:
                current.right.next = current.next.left if current.next else None
                q.append(current.right)
        return root
                
              
        
         