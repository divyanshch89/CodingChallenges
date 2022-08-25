#Link  - https://leetcode.com/problems/copy-list-with-random-pointer/
from operator import ne
from typing import Optional


class Node:
    def __init__(self,val,next,random) -> None:
        self.val = val
        self.next = next
        self.random = random
class Solution:
    '''
    TC= O(N)
    SC= O(N)
    '''
    def copyRandomList(self, head: Node,visited={}):
        #Linkedlist problems can be seen as tree or graph problems and vice versa
        #here we are going to visualize the LL as a graph and try to traverse it
        if not head:
            return
        if head in visited:
            return visited[head]
        visited[head] = Node(head.val,None,None)
        visited[head].next = self.copyRandomList(head.next,visited)
        visited[head].random = self.copyRandomList(head.random,visited)
        return visited[head]

'''
TC = O(N)
SC - O(1) -  as we are modifiying in place
'''
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return head
#         current =head
        
#         #this should create an interweaved list
#         while current:
#             newNode = Node(current.val,current.next,None)
#             current.next =newNode
#             current = newNode.next
        
#         #lets set the random reference
#         current =head
#         while current and current.next:
#             newNode = current.next
#             newNode.random = current.random.next if current.random else None
#             current = current.next.next
            
#         #remove the old nodes
#         pt_old_head = head
#         pt_new_head = head.next
#         new_head = head.next
#         while pt_old_head:
#             pt_old_head.next = pt_old_head.next.next if pt_old_head.next else None
#             pt_new_head.next = pt_new_head.next.next if pt_new_head.next else None
#             pt_old_head = pt_old_head.next
#             pt_new_head = pt_new_head.next
#         return new_head