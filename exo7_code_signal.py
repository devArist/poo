from random import randint

def almostIncreasingSequence(sequence):
    success = None
    random_index = randint(0, len(sequence)-1)
    remove = sequence.pop(random_index)
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            success = True
        else:
            success = False
            # return success
    return remove

print(almostIncreasingSequence([23, 4, 12, 39]))