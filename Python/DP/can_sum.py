from typing import List

#Before memoization
#TC - O(n^m) - #of of branching ^ height of the tree
#SC - O(m)

#After memoization
#TC = O(m*n) where n is length of numbers and m is the target
#SC = O(m) - depth of the tree
def canSum(target:int, numbers:List[int],memo={}) -> bool:
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for n in numbers:
        rem = target-n
        if canSum(rem,numbers,memo):
            memo[target]=True
            return True
    memo[target]= False
    return False


print(canSum(7,[2,3],{})) #true
print(canSum(7,[5,3,4,7],{})) #true
print(canSum(7,[2,4],{})) #false
print(canSum(8,[2,3,5],{})) #True
print(canSum(300,[7,14],{}))#false