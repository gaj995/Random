def can_construct(target, array):
    table = [False] * (len(target)+1)
    table[0] = True

    for index, value in enumerate(table):
        if value == True and index < len(target):
            letter = target[index]
            for word in array:
                if target[index : index + len(word)] == word:
                    table[index + len(word)] = True
                    

    return table[-1]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeg', ['e', 'ee', 'eeee', 'eeeeeeee', 'eeee', 'eeee', 'asdasd']))
