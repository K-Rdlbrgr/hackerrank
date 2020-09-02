# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    # We start with assigning two variables which we need to iterate through
    # the values of the array. 'i' represents the first value in the array and
    # 'temp_max' represents the maimum of the first two values.
    i, temp_max = arr[0], max(arr[:2])

    # This loop executes the actual work of the function by iterating over the
    # array, starting by the third value of the array, up until the last value
    # of it.
    for val in arr[2:]:
        # While looping through the array, the function identifies the maximum
        # between (1) the last value, (2) the second to last value, (3) the second
        # to last value + the current value and (4) the current value. This
        # maximum will update the temp_max and the old temp_max replaces the i
        # value.
        i, temp_max = temp_max, max(i, i + val, temp_max, val)

    # Finally, we return the maximum after looping through the entire array
    return temp_max


# Test
array = [3, 7, 4, 6, 5]

print(maxSubsetSum(array))
