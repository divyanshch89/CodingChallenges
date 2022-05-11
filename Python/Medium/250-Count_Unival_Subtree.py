'''
Link - https://leetcode.com/problems/count-univalue-subtrees/
Approach - Given a node in our tree, we know that it is a univalue subtree if it meets one of the following criteria:

-> The node has no children (base case)
-> All of the node's children are univalue subtrees, and the node and its children all have the same value
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,val):
        if not root:
            return True
        if not all([self.helper(root.left,root.val),
                   self.helper(root.right,root.val)]):
            return False
        #if we here that means that we are at the leaf or at the root of valid uni-tree
        self.count+=1
        return root.val == val
        
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.helper(root,0)
        return self.count
        