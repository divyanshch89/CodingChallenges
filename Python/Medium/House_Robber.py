#Link -  https://leetcode.com/problems/house-robber/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Recursive:
        TC = O(2^N) where N is len of nums
        SC = O(N) depth/height of recursion tree
        
        Memoized:
        TC = O(N)
        SC = O(N) , the memo object can have upto N keys
        '''
        return self.robFrom(0,nums,{})
    def robFrom(self,pos,nums,memo={}):
        '''This is a DP solution where starting from pos=0, robber has 2 choices either leave the current house and move to pos+1 or 
        steal from the current house nums[pos] and move to next to next house i.e nums[pos]+ move to pos+2
        '''
        if pos in memo: return memo[pos]
        if pos>=len(nums):
            return 0
        memo[pos] = max(self.robFrom(pos+1,nums,memo),nums[pos]+self.robFrom(pos+2,nums,memo))
        return memo[pos]
            