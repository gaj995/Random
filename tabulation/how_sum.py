def can_sum(target_sum, array):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i, value in enumerate(table):
        if value != None:
            for num in array:
                if i + num < len(table):
                    table[i + num] = value + [num]
    return table[target_sum]

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
