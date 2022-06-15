class TreeNode:
    def __init__(self,val=0, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val
class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
