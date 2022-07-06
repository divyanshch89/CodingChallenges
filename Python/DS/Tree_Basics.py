#Observation:
#first print the root and then left and right child
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

class TreeInfo:
    def __init__(self,diam,height) -> None:
        self.diam = diam
        self.height = height

class BinaryTree:
    def __init__(self) -> None:
        self.idx = -1
    def buildTree(self,nodes):
        #TC: O(N) - it will touch all indexes of the list nodes
        self.idx+=1
        if nodes[self.idx]==-1:
            return
        #create a new node
        newNode = Node(nodes[self.idx])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)
        return newNode
    
    def preorder(self, node: Node):
        if not node:
            print(str(-1), end= " ")
            return
        print(str(node.val), end= " ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    def countOfNodes(self, node:Node):
        #TC - O(N)
        if not node:
            return 0
        leftTreeCount = self.countOfNodes(node.left)
        righTreeCount = self.countOfNodes(node.right)
        return 1+ leftTreeCount + righTreeCount
    
    def sumOfNodes(self, root: Node):
        if not root:
            return 0
        leftSum = self.sumOfNodes(root.left)
        rightSum = self.sumOfNodes(root.right)
        return root.val+leftSum+rightSum
    
    def height(self, root: Node):
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return 1 + max(leftHeight, rightHeight)
    
    def diameter(self, root: Node):
        #Observations:
        """
        Case 1: The diam passes through the root node
        The longest path will be the height (LT) + height(RT)+1
        Case 2 : The diam doesn't passes thorough the root, in that case, the diam will be max(Diam(LT),Diam(RT))
        """
        #TC: ON(N^2) as we for every node we visit to cal the diam, we are visiting N nodes to cal height
        #base case
        if not root:
            return 0
        left_diam = self.diameter(root.left)
        right_diam = self.diameter(root.right)
        tot_height = self.height(root.left)+self.height(root.right)+1
        return max(tot_height, max(left_diam, right_diam))
    
    def diameter_optimized(self,root):
        '''
        Observations:
        We can cal diam and height at every node level instead of traversing twice for cal diam and height as in previous approach
        '''
        if not root:
            return TreeInfo(0,0)
        
        left_info = self.diameter_optimized(root.left)
        right_info = self.diameter_optimized(root.right)
        # height of the current node
        node_ht = 1 + max(left_info.height, right_info.height)
        # left and right diam and tot_height are needed to cal the diam at the current node
        left_diam = left_info.diam
        right_diam = right_info.diam
        tot_height = left_info.height+right_info.height+1

        node_info = TreeInfo(0,0)
        node_info.height = node_ht
        node_info.diam = max(tot_height, max(left_diam, right_diam))
        return node_info

#driver code
nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
tree = BinaryTree()
root = tree.buildTree(nodes)
print(f"# of nodes in tree: {tree.countOfNodes(root)}")
print(f"Sum of all nodes in tree: {tree.sumOfNodes(root)}")
print(f"Tree Height: {tree.height(root)}")
print(f"Tree Diameter: {tree.diameter(root)}")
print(f"Tree Diameter Optimized: {tree.diameter_optimized(root).diam}")
tree.preorder(root)


