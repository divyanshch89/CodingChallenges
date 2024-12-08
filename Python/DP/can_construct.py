'''
Complexity Analysis:
N - length of wordBank
M - length of target

Before:

TC - O(N^M*M) - branching factor ^ len of target * line 13 will take O(M) time to get the index
SC - O(M*M) - max there is will M frames in the call stack and each frame will hold the suffix of len M

After:
 TC - (N*M*M)
 SC - O(M*M)
'''
def canConstruct(target,wordBank,memo={}):
    if target in memo: return memo[target]
    if target == '': return True
    for word in wordBank:
        if word in target and target.index(word)== 0:
            # we can construct the target from the given work
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank):
                # if any of the branches return True, we will do an early return
                memo[target] = True
                return True
    # if we are here, then we have tried all the combinations and couldn't resolve to true
    memo[target] = False
    return False



print(canConstruct('abcdef',
                    ['a','bc','def']
                    )) # True
print(canConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf',
                    ['a','aa','aaa','aaaa','aaaaa','aaaaaa']
                    )) # False