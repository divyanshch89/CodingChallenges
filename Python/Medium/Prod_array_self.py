#Link  - https://leetcode.com/problems/product-of-array-except-self/
from ast import List


class Solution:
    '''
    TC - O(N)
    SC - O(N)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        Left,Right,result = [0]*length, [0]*length, [0]*length
         #for left prod array, first elem should be 1 and last for right
        Left[0], Right[length-1] = 1,1
        
        #cal the prod of all the elems to the left of current
        for i in range(1, length):
            Left[i] = Left[i-1]*nums[i-1]
        #cal the prod of all the elems to the right of current
        for i in range(length-2, -1,-1):
            Right[i] = Right[i+1] * nums[i+1]
        #get the final result by taking prod of elems in both left and right array
        for i in range(0,length):
            result[i]=Left[i]*Right[i]
        return result


'''The space optimised version. The output array will not be counter towards SC'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        Left= [0]*length
        Left[0]=1
        
        #cal the prod of all the elems to the left of current
        for i in range(1, length):
            Left[i] = Left[i-1]*nums[i-1]
       #the right can be calculated on the fly
        R = 1
        for i in range(length-2, -1,-1):
            R = R * nums[i+1]
            Left[i] = Left[i] * R
        return Left
