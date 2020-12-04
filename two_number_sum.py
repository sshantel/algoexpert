def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        first = array[i]
        for j in range(i + 1, len(array)):
            print(j)
            second = array[j]
            if first + second == targetSum:
                return [first, second]
    return []

