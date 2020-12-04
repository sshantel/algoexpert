def isValidSubsequence(array, sequence):
    # create two pointers
    seq = 0
    for value in array:
        if seq == len(sequence):
            break
        if sequence[seq] == value:
            seq += 1

    return seq == len(sequence)

