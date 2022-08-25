from typing import List

#Before memoization
#m =  target sum and n = len(numbers)
#TC - O(n^m*m) - #of of branching ^ height of the tree
#SC - O(m*m) - call stack call is holding on to shortest list which can have max length of m (consider target sum =3, numbers=[1], the result would be [1,1,1])

#After memoization
#TC = O(m*n) where n is length of numbers and m is the target
#SC = O(m) - depth of the tree
def bestSum(target:int, numbers:List[int],memo={}):
    if target in memo: return memo[target]
    if target==0: return []
    if target<0: return None
    shortest = None
    for num in numbers:
        remTarget = target-num
        result = bestSum(remTarget,numbers,memo)
        if type(result) is list:
            result.append(num)
            #if the current result is shorter than the "shortest" then,update it
            if not shortest or len(shortest)> len(result):
                shortest=result
    memo[target]=shortest
    return shortest    



    



print(bestSum(7,[5,3,4,7],{})) #[7]
print(bestSum(8,[2,3,5],{})) #[5,3]
memo1 = {}
print(bestSum(8,[1,4,5],memo1)) #[4,4]
print(memo1)
# print(bestSum(100,[1,2,5,25],{})) #[25,25,25,25]