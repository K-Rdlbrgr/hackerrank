def arrayManipulation(n, queries):
    # Creation of a list of zeros with the length (n+1)
    arr = [0 for i in range(0, n + 1)]
    # Assigning count and result which will be used to calculate the max number later on
    count = 0
    result = 0

    # Looping through the querries to manipulate the created array 'arr'
    for first, last, value in queries:

        # The first index which gets manipulated is incremented by the corresponding value
        arr[first] += value
        # The first index after the last manipulated entry gets reduced by the
        # same value in order to see where the incrementation ended, so the
        # function can calculate the max later on.
        if (last != len(arr) - 1):
            arr[last + 1] -= value

    # Once the manipulation of the array is finished, the loop sums the values
    # up from the start and updates the curretn maximum each time in case the
    # count is actually larger than the result
    for number in arr:
        count += number
        if count > result:
            result = count

    # Returning the maximum number in the array (result)
    return result


# Test
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
n = 10

print(arrayManipulation(n, queries))


# Intuitive solution

# This solution, while being shorter and more intuitive is not efficient
# enough to pass the time constraints of the challenge


def arrayManipulationIntuitive(n, queries):
    # Creation of a list of zeros with the length (n+1)
    arr = [0 for i in range(0, n)]

    # Looping through the querries to increment all values within the corresponding range
    for first, last, value in queries:
        for i in range(first - 1, last):
            arr[i] += value

    # Returning the maximum number in the array (result)
    return max(arr)
