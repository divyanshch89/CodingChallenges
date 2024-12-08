class My_MergeSort:
    def __init__(self,arr):
        self.arr = arr
    def sort(self):
        return self.split(self.arr)
    def split(self,arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        #split left
        left = self.split(arr[:mid])
        #split right
        right = self.split(arr[mid:])        
        return self.merge(left,right)
    def merge(self,left,right):
        #TC - O(N)
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #push left to the result and increament
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        #if we are here then it is possible that one of the array is yet to be merged
        while i < len(left):
            result.append(left[i])
            i+=1
        while j < len(right):
            result.append(right[j])
            j+=1
        return result
        

def caller():
    # input = [11,9,12,7,3]
    input = [11,24,9,12,13,7]
    my_sort = My_MergeSort(input)
    result = my_sort.sort()
    print(result) # [3,7,9,11,12]

caller()
  
