#TC - O(n) where n is length of s2
#SC - O(1)
class Solution:
    def matches(self,arr1,arr2):
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #observation
        # we are trying to see an anagram of s1 exist in s2
        if len(s1)> len(s2):
            return False
        arr_s1 = [0]*26
        arr_s2 = [0]*26
        left = 0
        right = 0
        while right<len(s1):
            arr_s1[ord(s1[right])-ord('a')]+=1
            arr_s2[ord(s2[right])-ord('a')]+=1
            right+=1
       
        #moving right pointer back to the end of the window
        right-=1
        
        while right <len(s2):
            if self.matches(arr_s1,arr_s2):
                return True
            right+=1
            #add the next char from s2 to the hashmap array, 
            #only if the rightmost index is within the bounds of s2
            if right!=len(s2):
                arr_s2[ord(s2[right])-ord('a')]+=1
            #remove the leftmost char from the array
            arr_s2[ord(s2[left])-ord('a')]-=1
            #resize the window by moving the left towards right
            left+=1
        
        return False
            
            
        
        