import numpy as np

def map_strings_to_int(trainLabels):
    mapped_trainLabels = []
    dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'K': 9,
        'L': 10,
        'M': 11,
        'N': 12,
        'O': 13,
        'P': 14,
        'Q': 15,
        'R': 16,
        'S': 17,
        'T': 18,
        'U': 19,
        'V': 20,
        'W': 21,
        'X': 22,
        'Y': 23,
        'Z': 24,
    }

    for i in trainLabels:
        mapped_trainLabels.append(dict[i])

    return np.asarray(mapped_trainLabels,dtype='int64')