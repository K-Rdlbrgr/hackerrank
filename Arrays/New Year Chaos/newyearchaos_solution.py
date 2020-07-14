def minimumBribes(q):
    # Assining the inital number of bribes
    bribes = 0

    # Looping through the queue in order to check if each guest bribed another one in front of him or not
    for index, guest in enumerate(q):

        # In case, the guest bribed more than two people, the if condition prints
        # out that the queue is too chaotic and breaks the loop
        if guest - index > 3:
            return 'Too chaotic'

        # If a certain guest is within his 2 bribe limit, the function loops again
        else:
            # This time the function loops only between the guest's original position
            # (guest) and the guest's current position (index) in order to check if
            # the guest got bribed or not. Doing it this way allows to loop through
            # the whole list every single time which reduces the execution time for
            # extensive lists. With the max function, it is avoided to have indeces
            # below 0.
            for check in range(max(guest - 2, 0), index):
                if q[check] > guest:
                    bribes += 1
                else:
                    pass

    # Finally we return the bribes
    return bribes


# Test
queue = [1, 2, 5, 3, 7, 8, 6, 4]

print(minimumBribes(queue))
