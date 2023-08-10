class LocalStack:
    def __init__(self) -> None:
        self.capacity = 2
        self.arr = [None]*self.capacity
        self.top = -1
    
    def IsEmpty(self):
        return self.top==-1
    
    def GetTop(self):
        return self.arr[self.top]
    
    def push(self, item):
        #check if we have space in the current array
        #if yes, then increament the top and push the item in the array
        #if not, then resize the array and then insert
        if self.top == len(self.arr)-1:
            #time to resize the array
            self.capacity *= 2
            new_arr = [None]* self.capacity
            #copy the values from old array to the new one
            for i in range(len(self.arr)):
                new_arr[i] = self.arr[i]
            #update the old array ptr to the new one
            self.arr = new_arr
        #since resizing is done, we perform the usual push operation
        self.top+=1
        self.arr[self.top]= item

    
    def pop(self):
        if not self.IsEmpty():
            item = self.arr[self.top]
            #reduce the top
            self.top-=1
            return item
        return -1

def testMethod():
    st = LocalStack()
    print("Is stack empty - "+ str(st.IsEmpty()))
    st.push(1)
    st.push(2)
    print(st.GetTop())
    print("Is stack empty - "+ str(st.IsEmpty()))
    st.push(4)
    st.pop()
    st.pop()
    print(st.GetTop())
    print("Is stack empty - "+ str(st.IsEmpty()))
    st.push(5)
    st.push(6)
    st.push(7)
    print(st.GetTop())
    print(st.arr)

testMethod()
