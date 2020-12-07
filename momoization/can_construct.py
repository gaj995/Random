def can_construct(target, array, memo={}):
    if target in memo:
        return memo[target]
    elif target == '':
        return True

    for word in array:
        if target[:len(word)] == word:
            suffix = target[len(word):]
            if can_construct(suffix, array, memo) == True:
                memo[target] = True
                return memo[target]

    memo[target] = False
    return memo[target]

print (can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print (can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print (can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print (can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeg', ['e', 'ee', 'eeee', 'eeeeeeee', 'eeee', 'eeee', 'asdasd']))
