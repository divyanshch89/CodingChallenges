#Link - https://leetcode.com/problems/next-greater-element-i/description/
#Time - 
#Space - 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        the greatest number to the current is always to the right (in reverse order). So
        we can use stack to keep track of numbers lesser than current
        '''
        master ={}
        st =[]
        result =[]
        for num in nums2:
            while st and st[-1] <num:
                #for the top item on stack, num is next greater number
                master[st[-1]]=num
                #remove the last/top item from the stack
                st.pop()
            #now push the current item for next comparison
            st.append(num)
        for s in st:
            master[s]=-1
        for num in nums1:
            result.append(master[num])
        return result

        
