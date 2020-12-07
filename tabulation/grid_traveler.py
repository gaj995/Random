def grid_travel(m, n):
    table = [[0] * (n+1) for i in range(m+1)]
    table[1][1] = 1

    for row, val in enumerate(table):
        for column, v in enumerate(val):
            if row + 1 <= m:
                table[row + 1][column] += table[row][column]
            if column + 1 <= n:
                table[row][column + 1] += table[row][column]

    return table[m][n]
            

print (grid_travel(2, 3))
print (grid_travel(1, 1))
print (grid_travel(18, 18))
