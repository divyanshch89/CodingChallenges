'''
TC = O(N^2)
SC = O(N) - to store the result
'''
from typing import List


class Solution:
    def TwoSum(self,i,nums,res):
        low,high = i+1,len(nums)-1
        while low < high:
            cur_sum = nums[i]+nums[low]+nums[high]
            if cur_sum<0:
                #the sum of low and high is not high enough to drive the total sum to 0
                low+=1
            elif cur_sum>0:
                high-=1
            else:
                #we found the right triplet
                res.append([nums[i],nums[low],nums[high]])
                low+=1
                high-=1
                while low < high and nums[low-1]==nums[low]:
                    low+=1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        For this approach to work we need a sorted list
        Take a number as pivot and use 2 pointer approach to see if we can find a
        a triplet whose sum will be 0, and then move to a new pivot
        '''
        res =[]
        #O(NLogN)
        nums.sort()
        #O(N)
        for i in range(len(nums)):
            if nums[i]>0:
                #this is a fail condition because in a sorted array all numbers will be + and we can 
                #never find a triplet with sum =0
                break
            if i==0 or nums[i-1]!=nums[i]:
                #O(N)
                self.TwoSum(i,nums,res)
        return res
        