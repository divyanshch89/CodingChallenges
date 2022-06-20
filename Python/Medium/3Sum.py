class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2step process
        #First:
            # select the pivot (at index 1) and if pivot is greater than 0 then no pair whose             #sum
            # can be 0 can exist as the array is already sorted
        #Second:
        #perform two steps on the sorted array and find the sum of current index i and low and high numbers
        
        res = []
        #TC - O(NLogN)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            #the below condition is to avoid adding dups
            if i==0 or nums[i-1]!=nums[i]:
                self.TwoSum(nums,i,res)
        return res
    def TwoSum(self,nums,i,res):
        lo,high = i+1, len(nums)-1
        while lo <high:
            sum = nums[i]+nums[lo]+nums[high]
            if sum <0:
                #the current pair of low and high is not big enough to bring the total to 0
                lo+=1
            elif sum >0:
                high-=1
            else:
                #we found the right combinations
                res.append([nums[i],nums[lo],nums[high]])
                lo+=1
                high-=1
                while lo < high and nums[lo]==nums[lo-1]:
                    #to avoid any duplicate values
                    lo+=1
                
        