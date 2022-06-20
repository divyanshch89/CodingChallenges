#Link - https://leetcode.com/problems/happy-number/
#Time - 
#Space - 
class Solution:
    def getNext(self,n):
        sum = 0
        while n:
            rem =n%10
            sum+=rem**2
            n//=2
        return sum
    def HappyNumber(self,n):
        #we can use the Floyd's cycle detection alogrithm
        slow = n
        fast = n
        while fast!=1:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
            if slow==fast:
                #there is a cycle detected
                return False
        return fast==1
