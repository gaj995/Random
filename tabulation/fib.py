def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i, val in enumerate(table):
        try:
            table[i + 1] += table[i]
            table[i + 2] += table[i]
        except:
            pass

    return table[n]

print(fib(6))
print(fib(200))
