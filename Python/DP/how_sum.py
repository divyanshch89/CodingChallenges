from typing import List

#Before memoization
#TC - O(n^m*m) - #of of branching ^ height of the tree*at most m operations for the append operation(copy array over to accomodate extra elem)
#SC - O(m)

#After memoization
#TC = O(n*m*m) where n is length of numbers and m is the target
#SC = O(m*m) - this the space of the memo object which will at most have m keys and at most m values per key
def howSum(target, numbers,memo={}):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for n in numbers:
        rem = target-n
        returnVal = howSum(rem,numbers,memo)
        if type(returnVal) is list:
            returnVal.append(n)
            memo[target] = returnVal
            return returnVal
    memo[target]=None
    return None

mem={}
print(howSum(7,[2,3],mem)) #true
print(mem)
print(howSum(7,[5,3,4,7],{})) #true
print(howSum(7,[2,4],{})) #false
print(howSum(8,[2,3,5],{})) #True
print(howSum(300,[7,14],{}))#false