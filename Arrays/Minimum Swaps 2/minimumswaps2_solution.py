def minimumSwaps(arr):
    # Assigning initial swap counter and an empty dictionary for the indeces
    swap_counter = 0
    indeces = {}

    # Looping through the array of numbers, saving them as keys and their indeces as values
    for i, entry in enumerate(arr):
        indeces[entry] = i

    # Looping through the array again to order it and count the swaps
    for ind, number in enumerate(arr):
        # In case the number is already at it's right place, the funtion continues to the next number
        if number == ind + 1:
            continue
        # Otherwise the current number at a specific index gets swaped with the correct number for this index and the coresponding entries in the dictionary, containing the indeces gets updated
        else:
            arr[ind], arr[indeces[ind+1]] = arr[indeces[ind+1]], arr[ind]
            indeces[number], indeces[ind+1] = indeces[ind+1], indeces[number]
            swap_counter += 1

    # Returning the amount of swaps
    return swap_counter

# To be more efficient, a dictionary is used to store the indeces and used to find the correct index for a specific number. Leaving the dictionary out and using the built-in .index function every time a index for a number needs to be picked would result in a longer run-time, since the index functions has to loop through the whole array


# Test
arr = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(arr))
