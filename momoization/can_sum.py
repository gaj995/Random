def can_sum(target_sum, array, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return True
    elif target_sum < 0:
        return False

    for num in array:
        remainder = target_sum - num
        if can_sum(remainder, array, memo) == True:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False
