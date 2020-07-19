# First we import defaultdict from collections
from collections import defaultdict


def isValid(s):
    # Using the Counter function to count all appearances of every character within the string
    count = Counter(s)
    # Counting the frequencies of all the appearances within the string
    freq = Counter(count.values())

    # If every character appear the exact same amount of times, the length of
    # frequency is equal to one and we can return 'YES'
    if len(freq) == 1:
        return "YES"

    # Otherwise the length of frquency can only be 2, since more than 2
    # different frequencies would result in an unvalid string
    elif len(freq) == 2:
        # Here we need to extract the maximum and minimum key of the frequency
        key_max = max(freq.keys())
        key_min = min(freq.keys())

        # If the differnce between them is 1 and the number of the higher
        # frequency is also just 1, the string can be adhusted by removing one
        # character and is therefore ruled as valid
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        # Another case for a valid string would be if the appearances of the
        # minimum key is only one and we can drop this character to generate an
        # equal amount of appearances for each character
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"

    # If no check is passed return 'NO'
    return "NO"


# Test
string = 'aabbc'

print(isValid(string))
