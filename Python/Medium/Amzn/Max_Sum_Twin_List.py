
#Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''Recursive solution where we traverse till the end of the linkedlist and then recurse back with the updated value of left ptr'''
    def pairSum(self, head: Optional[ListNode]) -> int:
        left = head
        def traverse(node):
            if not node:
                return 0
            nonlocal left
            cur_max = max(traverse(node.next),node.val+left.val)
            left = left.next
            return cur_max
        return traverse(head)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''Create a list from the linked list and then cal max sum of the pairs
        TC: O(N)
        SC  -O(N)
        '''
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums_Len = len(nums)
        max_sum = nums[0]
        for i in range(nums_Len):
            max_sum = max(max_sum, nums[i]+nums[nums_Len-1-i])
        return max_sum

