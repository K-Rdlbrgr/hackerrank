def alternatingCharacters(s):
    # Assigning the first character of the string as the initial check string
    check = s[0]

    # Assigning the initial check index 'j' and the initial counter
    j = 0
    counter = 0

    # Looping through each character pf the string, excluding the first one
    # since it is already assigned to the check as our reference
    for i in range(1, len(s)):
        # Checking i the current character of the string matches the last character in the check
        if s[i] != check[j]:
            # If it does, the character is appended to the check string and its index is incremented by 1
            check += s[i]
            j += 1
        # Otherwise the counter gets incremented by 1 since this would mean that a
        # character gets deleted in order to keep the alternation in the string
        else:
            counter += 1

    # Returning the number of deletions
    return counter


# Test
string = 'AAABBBAABB'

print(alternatingCharacters(string))
