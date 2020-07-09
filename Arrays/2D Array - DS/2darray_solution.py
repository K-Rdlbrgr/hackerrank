def hourglassSum(arr):
    # Creating empty list for all sums
    sums = []
    
    # Looping horugh each line and numbers in those lines, picking the right numbers by their index to construct the hourglass and sum them up
    for line in range(0,len(arr)-2):
        for number in range(0, len(arr[line])-2):
            temp_sum = sum(arr[line][number:number+3]) + arr[line+1][number+1] + sum(arr[line+2][number:number+3])
            
            # Appending the temporary sum to the sum list
            sums.append(temp_sum)
    
    # Returning the maximum sum
    return max(sums)


# Test
arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))