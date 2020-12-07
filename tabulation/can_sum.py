def can_sum(target_sum, array):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i, value in enumerate(table):
        if value == True:
            for num in array:
                if i + num < len(table):
                    table[i + num] = True
    return table[target_sum]

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
