#Leetcode Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_sz = 0
        for r, char in enumerate(s):
            if char in seen and left <=seen[char]:
                #the current char is seen already and within the current slide window
                left = seen[char]+1
            else:
                max_sz = max(max_sz,r-left+1)
            seen[char] = r
        return max_sz
        