class My_QuickSort:
    def __init__(self,arr):
        self.arr = arr
    def sort(self,start=0,end=None):
        #everytime sort is called, the len of sample input is reduced to halve
        #TC -O(logN)
        if end is None:
            end = len(self.arr)-1
        if start < end:
            pivot_index = self.partition(start,end)
            #sort the first halve
            self.sort(start, pivot_index-1)
            #sort the second halve
            self.sort(pivot_index+1,end)
        return self.arr
    def partition(self,start,end):
        #TC - O(N)
        pivot = self.arr[end]
        i = start-1
        for j in range(start, end+1):
            if self.arr[j] <pivot:
                i+=1
                self.arr[j],self.arr[i] = self.arr[i],self.arr[j]
                #increament i and swap i and j position
        #swap i+1 and end pos
        self.arr[i+1],self.arr[end] = self.arr[end],self.arr[i+1]
        return i+1
        

def caller():
    # input = [11,9,12,7,3]
    input = [11,24,9,12,13,7,3]
    my_sort = My_QuickSort(input)
    result = my_sort.sort()
    print(result) # [3,7,9,11,12]

caller()
  
