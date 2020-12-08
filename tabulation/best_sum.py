def can_sum(target_sum, array):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i, value in enumerate(table):
        if value != None:
            for num in array:
                if i + num < len(table):
                    comination = value + [num]
                    if (table[i+num]) == None or len(table[i+num]) > len(comination):
                        table[i + num] = comination
                        
    return table[target_sum]

print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(8, [1, 4, 5]))
print(can_sum(100, [1, 2, 5, 25]))
