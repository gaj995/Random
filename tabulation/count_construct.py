def can_construct(target, array):
    table = [0] * (len(target)+1)
    table[0] = 1

    for index, value in enumerate(table):
        for word in array:
            if target[index : index + len(word)] == word:
                table[index + len(word)] +=  value

    return table[-1]

print(can_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeg', ['e', 'ee', 'eeee', 'eeeeeeee', 'eeee', 'eeee', 'asdasd']))
