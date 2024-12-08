def countConstruct(target, wordBank,memo={}):
    if target in memo: return memo[target]
    if target == '': return 1
    constructCount = 0
    for word in wordBank:
        if word in target and target.index(word) == 0:
            constructCount+=countConstruct(target[len(word):],wordBank,memo)
    memo[target] = constructCount
    return constructCount


print(countConstruct('abcdef',
                    ['a','bc','def']
                    )) # 1
print(countConstruct('purple',
                    ['purp','p','ur','le','purpl']
                    )) # 2
print(countConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf',
                    ['a','aa','aaa','aaaa','aaaaa','aaaaaa']
                    )) # 0
print(countConstruct('enterapotentpot',
                    ['a','p','ent','enter','ot','o','t']
                    )) # 4