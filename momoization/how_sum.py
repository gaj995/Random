def how_sum(target_sum, array, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None

    for num in array:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, array, memo)
        if remainder_result != None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]
        
    memo[target_sum] = None
    return None

