#Link -https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        result = []
        last_visited = None
        current = root
        while st or current:
            while current:
                st.append(current)
                current = current.left
            current = st.pop()
            if current.right==None or current.right == last_visited:
                result.append(current.val)
                last_visited = current
                current =  None
            else:
                st.append(current)
                current = current.right
        return result