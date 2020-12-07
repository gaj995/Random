def all_construct(target, array):
    if target == '':
        return [[]]

    result = []

    for word in array:
        if target[:len(word)] == word:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, array)
            traget_ways = [i.append(word) for i in suffix_ways]
            result = result + suffix_ways

    return result

print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
