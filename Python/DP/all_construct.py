def allConstruct(target,wordBank,memo={}):
    if target in memo: return memo[target]
    if target == '': return [[]]
    main_result = []
    for word in wordBank:
        if word in target and target.index(word) == 0:
            # only break the target when the curren word is the prefix
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix,wordBank,memo)
            for child in suffixWays:
                # for every child sub-array add the current word
                child.insert(0,word)
            # append it to the main result
            main_result+=suffixWays
    #memo[target] = main_result
    return main_result

print(allConstruct('purple',
                    ['purp','p','ur','le','purpl']
                    )) # 2
print(allConstruct('enterapotentpot',
                    ['a','p','ent','enter','ot','o','t']
                    )) # 4