#Link- https://leetcode.com/problems/implement-strstr/
# TC - O(n*m) where n is len of haystack and m is len of needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    #the haystack and needle doesnt match
                    break
                if j==len(needle)-1:
                    # we were able to match all the elems in j
                    return i
        return -1