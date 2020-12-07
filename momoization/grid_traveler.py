def grid_travel(x, y, memo={}):
    key = '{},{}'.format(x,y)
    
    if key in memo:
        return memo[key]
    elif x == 0 or y == 0:
        return 0
    elif x == 1 or y == 1:
        return 1
    
    memo[key] = grid_travel(x-1, y, memo) + grid_travel(x, y-1, memo)
    
    return memo[key]

