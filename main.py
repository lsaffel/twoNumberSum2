def twoNumberSum(array, targetSum):
    if len(array) == 1:
        return []

    for a in range(0, len(array)-1):
        for b in range(a+1, len(array)):
            if (array[a] + array[b]) == targetSum:
                return(array[a], array[b])

    return []
                    
    pass
