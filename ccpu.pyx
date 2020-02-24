from random import randint
import numpy as np
cimport numpy as np


cpdef np.ndarray[np.int, ndim=1] generator(int minV, int maxV, int amount):
    cdef np.ndarray[np.int, ndim=1] output = np.zeros[np.int, ndim=1]
    for iteration in range(amount):
        output.append(randint(minV, maxV))
    return output

cpdef np.ndarray[np.int, ndim=1] bubble_Sort(list input_data):
    cdef int number, swaps, i, j, t = 0
    cdef bint swapped = False

    cdef np.ndarray[np.int, ndim=1] data = input_data.copy()
    cdef short size = len(data)

    for j in range(size):
        swapped = False

        for i in range(0, size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

    return data
