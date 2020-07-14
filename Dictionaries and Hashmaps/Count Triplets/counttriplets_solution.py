# First we import defaultdict from collections
from collections import defaultdict


def countTriplets(arr, r):
    # Assigning the count variable
    count = 0

    # This dict stores number of tuples with two elements that can be formed if we find the key. It's initially empty
    potential_two_tuples = defaultdict(int)
    # This dict stores number of tuples with three elements that can be formed if we find the key. It's initially empty
    potential_three_tuples = defaultdict(int)
    # We assign the initial count with 0

    # Here the function loops through every element of the array, identifies the triplets and increments the count accordingly
    for i in arr:
        # The loop works in an order that only allows triplets once the last element of the triplet is found and the previous to elements are part of the potential_two_tuples dict

        # If i completes the three tuples given we have already found i/(r^2) and i/r, the count gets incremented by the amount of occurences in potential_three_tuples
        count += potential_three_tuples[i]

        # For any element of arr we can form three element tuples if we find i*r given i / r is already found while in this case i forms the second element. So, if i gets found in potential_two_tuples, the corresponding number in potential_three_tuples get incremented by it's occurences.
        potential_three_tuples[i*r] += potential_two_tuples[i]

        # For any element of arr we can form two element tuples if we find i*r while in this case i forms the first element. So, i*r in potential_two_tupels gets incremented by one for every r
        potential_two_tuples[i*r] += 1

    # Return the count
    return count


# Test
arr = [1, 3, 9, 9, 27, 81]
r = 3

print(countTriplets(arr, r))


# Intuitive solution

# This solution, while might being easier to understand is not efficient enough to pass the time constraints of the challenge


def countTripletsIntuitive(arr, r):
    # Assigning counter as an empty list
    counter = []

    # Looping through the array twice while starting the second loop one index further than the first loop in order to ensure that the second and third element of the triplet is occuring after the first element
    for i, number in enumerate(arr):
        for j in range(i+1, len(arr)):

            # The third loop again starts at the previous index. If the current number fulfills the condition that the three indeces are forming a geometrically increasing triplet with the base of r, the counter list appends all identified occurences of triplets to its list
            counter.append(sum([1 for i in range(j+1, len(arr)) if number*r == arr[j] == arr[i]/r]))

    # Return the sum of the count list
    return sum(counter)
