class Max_Heap:
    def __init__(self,capacity=5) -> None:
        self.capacity = capacity
        self.size = 0
        self.items = [0]*capacity
    
    def ensure_capacity(self):
        if self.size==self.capacity:
            #double the existing capacity and create a new item array
            self.capacity*=2
            temp = [0]*self.capacity
            for i in range(len(self.items)):
                temp[i] =self.items[i]
            self.items = temp
    
    def swap(self,src,des):
        self.items[src],self.items[des] = self.items[des],self.items[src]
    
    #heap helper functions to find indexes, parent and child items
    def get_parent_index(self,index):
        return (index-1)//2
    def get_left_child_index(self,index):
        return (index*2)+1
    def get_right_child_index(self,index):
        return self.get_left_child_index(index)+1
    
    def get_parent(self,index):
        return self.items[self.get_parent_index(index)]
    def get_left_child(self,index):
        return self.items[self.get_left_child_index(index)]
    def get_right_child(self,index):
        return self.items[self.get_right_child_index(index)]
    
    def has_parent(self,index):
        return self.get_parent_index(index)>=0
    def has_left_child(self,index):
        left_idx = self.get_left_child_index(index)
        return True if left_idx in range(1, len(self.items)) else False
    def has_right_child(self,index):
        right_idx = self.get_right_child_index(index)
        return True if right_idx in range(2, len(self.items)) else False
    
    #heapify up and down implementation
    def heapify_up(self):
        index = self.size-1
        #keep moving up as long as there is a parent and parent item < current item
        while self.has_parent(index) and self.get_parent(index)< self.items[index]:
            parent_idx = self.get_parent_index(index)
            self.swap(index,parent_idx)
            index = parent_idx

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            bigger_child = self.get_left_child_index(index)
            # if current node has the right child and its bigger than my left child then right becomes the bigger child
            if self.has_right_child(index) and self.get_right_child(index)> self.items[bigger_child]:
                bigger_child = self.get_right_child_index(index)
            
            #if current node is bigger than the bigger child then the heap properity is restore, exit the loop
            if self.items[index] > self.items[bigger_child]:
                break
            else:
                #swap the parent with the bigger child and continue
                self.swap(index,bigger_child)
                index = bigger_child
    
    #main max heap public methods

    def add(self, item):
        '''Add item to the heap and perform heapify up'''
        self.ensure_capacity()
        self.items[self.size] = item
        self.size+=1
        self.heapify_up()
    
    def poll(self):
        '''remove max item from the top of the heap and perform heapify down'''
        if self.size:
            item = self.items[0]
            self.items[0] = self.items[self.size-1]
            self.items[self.size-1] = 0
            self.size-=1
            self.heapify_down()
            return item
        print("Not enough items in the heap")
    
    def peek(self):
        if self.size:
            return self.items[0]
    
heap = Max_Heap()
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
