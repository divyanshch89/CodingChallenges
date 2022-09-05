#link -  https://leetcode.com/problems/subsets/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(nums,current_index,current_elem,result):
            if len(nums)==current_index:
                #TC - O(N)
                result.append(current_elem)
                return
            #The include and exclude 
            #include
            helper(nums,current_index+1,current_elem+[nums[current_index]],result)
            
            #exclude
            helper(nums,current_index+1,current_elem,result)
        helper(nums,0,[],result)
        return result
        
            
        