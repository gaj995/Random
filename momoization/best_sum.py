def best_sum(target_sum, array, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None

    shortest_combination = None

    for num in array:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, array, memo)
        if remainder_result != None:
           comination = remainder_result + [num]
           if shortest_combination == None or len(comination) < len(shortest_combination):
               shortest_combination = comination
               
    memo[target_sum] = shortest_combination
    return memo[target_sum]

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
