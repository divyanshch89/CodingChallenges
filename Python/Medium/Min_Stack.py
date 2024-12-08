class MinStack:

    def __init__(self,capacity = 5):
        self.capacity = capacity
        self.data = [0]*self.capacity
        self.topIndex = -1

    def ensureCapacity(self):
        if self.topIndex >=self.capacity-1:
            self.capacity*=2
            temp = [0]*self.capacity
            for item in self.data:
                temp.append(item)
            self.data = temp


    def push(self, val: int) -> None:
        self.ensureCapacity()
        if self.topIndex == -1:
            #the underline array is empty
            self.topIndex+=1
            self.data[self.topIndex] = [val,val]
        else:
            #get min_item from the current top
            min_val = self.data[self.topIndex][1]
            self.topIndex+=1
            self.data[self.topIndex] = [val,min(min_val,val)]
        

    def pop(self) -> None:
        #item = self.data[self.top]
        if self.topIndex>=0:
            self.data[self.topIndex] = 0
            self.topIndex-=1
        

    def top(self) -> int:
        return self.data[self.topIndex][0] if self.topIndex >=0 else -1
        

    def getMin(self) -> int:
        return self.data[self.topIndex][1] if self.topIndex >=0 else -1
        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
    # return 0
minStack.getMin() # return -2
minStack.top()