# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    # First we need to sort the values which allows us to avoid a second loop and make the function more efficient
    arr.sort()

    # Now the function uses a list comprehension to produce a list with all
    # absolute differences of the array and afterwards saves the minimal value
    # in the minimum variable
    minimum = min([(abs(arr[i] - arr[i + 1])) for i in range(len(arr) - 1)])

    # Finally the minimum gets returned
    return minimum


# Test
array = [1, 5, -6, -9, 10, 0]

print(minimumAbsoluteDifference(array))
