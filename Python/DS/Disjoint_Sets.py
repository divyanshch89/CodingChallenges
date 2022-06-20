class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjoinSet:
    def __init__(self) -> None:
        self.data_map= {}
    
    def makeSet(self,x):
        n = Node(x)
        n.parent = n
        self.data_map[x] = n
    def Union(self,x,y):
        #get the nodes
        n_x = self.data_map[x]
        n_y = self.data_map[y]

        #find the parent nodes
        p_x = self.Find(n_x)
        p_y = self.Find(n_y)
        if p_x.data==p_y.data:
            #if both parents are same, then do nothing
            return
        #otherwise parent node with higher rank becomes the parent of the other node
        if p_x.rank>=p_y.rank:
            p_x.rank = p_x.rank+1 if p_x.rank==p_y.rank else p_x.rank
            p_y.parent = p_x
        else:
            p_x.parent = p_y



    def FindSet(self, x):
        return self.Find(self.data_map[x]).data
    
    def Find(self, n:Node)->Node:
        if n.parent==n:
            return n
        #this path compresssion setting representative as the parent of all the child nodes
        n.parent = self.Find(n.parent)
        return n.parent

#driver code
ds= DisjoinSet()
ds.makeSet(1)
ds.makeSet(2)
ds.makeSet(3)
ds.makeSet(4)
ds.makeSet(5)
ds.makeSet(6)
ds.makeSet(7)

ds.Union(1,2)
ds.Union(2,3)
ds.Union(4,5)
ds.Union(6,7)
ds.Union(5,6)
ds.Union(3,7)

print(ds.FindSet(1))
print(ds.FindSet(2))
print(ds.FindSet(3))
print(ds.FindSet(4))
print(ds.FindSet(5))
print(ds.FindSet(6))
print(ds.FindSet(7))
