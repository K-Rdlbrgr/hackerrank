# First we import Counter and combinations
from collections import Counter
from itertools import combinations


def sherlockAndAnagrams(s):
    # Assigning an empty list for the count
    count = []

    # The for-loop and the list comprehension loop through the string and create
    for i in range(1, len(s) + 1):
        # The list comprehension goes through the string and gets all substrings
        # of a speciic length while also sorting it
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]

        # The Counter operator creates a dictionary out of the list of substrings,
        # counting the appearance of each of them
        b = Counter(a)

        # Here we loop through the Counter dictionary and use the combinations
        # function to create a list of lists of ('a', 'a') where the ('a', 'a')
        # stand for anagrams. The 'a' in the list comprehesion is completely
        # arbitrary and could be repalced by anything. K is set to 2 because the
        # function is looking for pairs of anagrams. Each ('a', 'a') counts for
        # one anagram, so the length stands for the anagram count of each
        # dictionary entry and the sum of it represents the anagram count of the
        # whole Counter object. Afterwards, the count gets appended to the count
        # list and the next loop starts, analysing substrings with one more
        # letter.
        count.append(sum([len(list(combinations(['a'] * b[j], 2))) for j in b]))

    # Return the sum of the count
    return sum(count)


# Test
string = 'abba'

print(sherlockAndAnagrams(string))


# Intuitive solution

# This solution, while might being easier to understand is not efficient
# enough to pass the time constraints of the challenge


def sherlockAndAnagramsIntuitive(s):
    # Assigning an initial counter and an empty list for all substrings
    counter = 0
    substrings = []

    # Looping through s and extracting all possible substrings while saving them in the corresponding list
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])

    # Looping through the extracted substrings, comparing if two substrings
    # are anagrams or not by using the Counter operator
    for index, sub in enumerate(substrings):
        for s in range(index + 1, len(substrings)):
            # The counter operator checks if two substrings have the same amount of
            # letters and consequently adds one to the counter if they do
            if Counter(sub) == Counter(substrings[s]):
                counter += 1

    # Return the counter
    return counter
