#Link -  https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        #we can check left and right balance
        # as long as we have enough * to balance then we are good and ignore the rest
        # but if the bal becomes negative then we can return false
        #because we cannot recover from having more closing paren then the opening + *
        left=0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='*':
                left+=1
            else:
                left-=1
            if left <0:
                return False
        if left ==0:
            return True
        right =0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or s[i]=='*':
                right+=1
            else:
                right-=1
            if right<0:
                return False
        return True