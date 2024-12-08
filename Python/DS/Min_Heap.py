class Min_Heap:
    def __init__(self,capacity=5) -> None:
        self.size = 0
        self.capacity = capacity
        self.items = [0]*self.capacity
    
    def ensureCapacity(self):
        if self.size==self.capacity:
            self.capacity*=2
            temp = [0]*self.capacity
            for i in range(self.size):
                temp[i] = self.items[i]
            self.items = temp
    
   #calculating indexes is most important
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self, index):
        return (index*2)+1
    def getRightChildIndex(self,index):
        return (index*2)+2
    
    def getParent(self,index):
        return self.items[self.getParentIndex(index)]
    def getLeftChild(self,index):
        return self.items[self.getLeftChildIndex(index)]
    def getRightChild(self,index):
        return self.items[self.getRightChildIndex(index)]
    
    def hasParent(self,index):
        return True if self.getParentIndex(index)>=0 else False
    def hasRightChild(self,index):
        return True if self.getRightChildIndex(index)> 1 and self.getRightChildIndex(index) < self.size else False
    def hasLeftChild(self,index):
        return True if self.getLeftChildIndex(index)>=1 and self.getRightChildIndex(index) < self.size else False

    def heapifyDown(self):
        '''First look at the left and right child and find the smallest. if the current parent > smallest child then swap or exit'''
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex =  self.getLeftChildIndex(index)
            rightChildIndex =  self.getRightChildIndex(index)
            if self.hasRightChild(index) and self.items[rightChildIndex] < self.items[smallerChildIndex]:
                #the right child is the small child
                smallerChildIndex = rightChildIndex
           
            #if parent is smaller than the smaller of the childs, then heap properity is restored
            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                 #swap the current_parent with the smaller child
                self.swap(index,smallerChildIndex)
                index = smallerChildIndex


    def heapifyUp(self):
        index = self.size-1
        #swap parent and child as long as there is a parent node (once you reach the root, this will help break out of the loop)
        # and the parent is > than the child (this is because of min heap)
        while self.hasParent(index) and self.getParent(index) > self.items[index]:
            parent_idx = self.getParentIndex(index)
            self.swap(index, parent_idx)
            index = parent_idx
    
    def swap(self, source, destination):
        self.items[source], self.items[destination] = self.items[destination], self.items[source]

    def add(self,val):
        '''
        Ensure there is capacity and always add the val to the end of the array
        '''
        self.ensureCapacity()
        self.items[self.size] = val
        self.size+=1
        self.heapifyUp()
    
    def peek(self):
        if self.size<0:
            print("No element in the heap")
            return
        return self.items[0]

    def poll(self):
        '''
        This removes the element from the array
        '''
        if self.size<0:
            print('cannot remove the element. Heap is empty')
            return
        #remove the root element
        item = self.items[0]
        #move the last element to the top
        self.items[0] = self.items[self.size-1]
        #reset the last item to 0
        self.items[self.size-1]=0
        self.size-=1
        self.heapifyDown()
        return item

heap = Min_Heap()
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

