# First we import the Counter operator
from collections import Counter


def checkMagazine(magazine, note):
    # The counter operator creates a dictionary for the note and the magazine with the counts of each word. The functions afterwards substracts the magazine dict from the note dict and compares it too an empty dict.
    if (Counter(note) - Counter(magazine)) == {}:
        # In case all words of the note are available enough times in the magazine the result is an empty dict and the functions returns 'Yes'
        return print('Yes')
    else:
        # In case some word is missing, the functions returns 'No'
        return print('No')


# Test
magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']

print(checkMagazine(magazine, note))
# Intuitive solution

# This solution, while might being easier to understand is not efficient enough to pass the time constraints of the challenge


def checkMagazineIntuitive(magazine, note):
    # Loop through the note and check if the word is in the magazine
    for word in note:
        if word in magazine:
            # In case the word is in the magazine, the word gets removed from the magazine list to ensure it does not get used multiple times for the note
            magazine.remove(word)
            continue
        # In case a word of the note is missing, the function returns 'No'
        else:
            return print('No')
    return print('Yes')
