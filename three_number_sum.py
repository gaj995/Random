def three_number_sum(array, targetSum):
    array.sort()
    triplets = []
    for index, value in enumerate(array):
        left = index + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[index] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[index], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1
    return triplets

print (three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
