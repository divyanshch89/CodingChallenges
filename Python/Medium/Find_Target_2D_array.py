from re import search

'''
TC = O(RLogC) where R is # of rows and C is # of cols
SC = O(1)
'''
class Solution:
    def is_target_exist(self,target, array):
        '''
        We can solve this problem in 2 steps:
        1. Find the row where the target exists:
            1.1 since the rows in the 2d array are sorted we can check if the target between the lower and the upper bound
        2. Once the desired array is found, we will use binary search to determine if the target exist or not
        '''
        row = len(array)
        col = len(array[0])
        for i in range(row):
            lower_bound = array[i][0]
            upper_bound = array[i][col-1]
            if target >=lower_bound and target<=upper_bound:
                #this row potentially has the target
                return self.search(target,array[i])
        return False
    
    def search(self,target,nums):
        left = 0
        right = len(nums)-1
        while left <=right:
            mid = left+ (right-left)//2
            if nums[mid]<target:
                #move left
                left = mid+1
            elif nums[mid]>target:
                #move right
                right= mid-1
            else:
                #we have the result
                return True
        return False


test_arry = [[2,3,4,5],
             [7,8,9,11],
             [13,15,18,20]]
sol =  Solution()
print(sol.is_target_exist(15,test_arry))