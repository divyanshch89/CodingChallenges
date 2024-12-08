class Min_Heap_Copy:
    def __init__(self,capacity=5) -> None:
        self.size = 0
        self.capacity = capacity
        self.items = [0]*self.capacity
    
    #helper methods
    def ensureCapacity(self):
        if self.capacity == self.size:
            #double the current capacity
            self.capacity*=2
            temp = [0]*self.capacity
            for i in range(self.size):
                temp[i] = self.items[i]
            self.items = temp
    
    #helper - find index methods
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self, index):
        return (index*2)+1
    def getRightChildIndex(self,index):
        return (index*2)+2
    
    def hasParent(self,index):
        return True if self.getParentIndex(index)>=0 else False
    def hasLeftChild(self,index):
        return True if self.getLeftChildIndex(index)>=1 and self.getLeftChildIndex(index) < self.size else False
    def hasRightChild(self,index):
        return True if self.getRightChildIndex(index)>1 and self.getRightChildIndex(index) < self.size else False
    def getParent(self,index):
        return self.items[self.getParentIndex(index)]
    
    def swap(self, source, destination):
        self.items[source], self.items[destination] = self.items[destination],self.items[source]
    
    def heapifyUp(self):
        #as long as parent < current index keep swapping and move the element up
        index = self.size-1
        while self.hasParent(index) and self.items[index] < self.getParent(index):
            parentIndex =  self.getParentIndex(index)
            self.swap(index,parentIndex)
            index = parentIndex

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex,rightChildIndex = self.getLeftChildIndex(index),self.getRightChildIndex(index)
            if self.hasRightChild(index) and self.items[smallerChildIndex] > self.items[rightChildIndex]:
                smallerChildIndex = rightChildIndex
            #check if the heap property is restored ie parent < smaller of the two childs
            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                self.swap(index,smallerChildIndex)
                index =smallerChildIndex


    #main class methods

    def add(self,item):
        self.ensureCapacity()
        #all additions are made to the end of the items list
        self.items[self.size] = item
        self.size+=1
        self.heapifyUp()
    
    '''
    get the root of the heap
    '''
    def peek(self):
        if len(self.items) == 0:
            return -1000
        return self.items[0]
    
    def poll(self):
        if len(self.items)==0:
            return -1000
        item = self.items[0]
        #put last item as the root
        self.items[0] = self.items[self.size-1]
        self.items[self.size-1] = 0
        self.size-=1
        self.heapifyDown()
        return item

    
    
   
    
    
   

heap = Min_Heap_Copy()
heap.add(5)
heap.add(6)
heap.add(4)
heap.add(1)
heap.add(10)
heap.add(11)
heap.add(3)
print(f'the root is :{heap.peek()}')
print(f'the items in the heap :{heap.items}')
print(f'Polled item :{heap.poll()}')
print(f'the root is :{heap.peek()}')
print(f'the items in the heap :{heap.items}')
print(f'Polled item :{heap.poll()}')
print(f'Polled item :{heap.poll()}')
print(f'the root is :{heap.peek()}')
print(f'the items in the heap :{heap.items}')
print(f'Polled item :{heap.poll()}')
print(f'the root is :{heap.peek()}')
print(f'the items in the heap :{heap.items}')
print(f'Polled item :{heap.poll()}')
print(f'the root is :{heap.peek()}')
print(f'the items in the heap :{heap.items}')

