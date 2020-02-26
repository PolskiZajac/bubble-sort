from random import randint
import numpy as np
cimport numpy as np


cpdef np.ndarray[long, ndim=1] generator(long minV, long maxV, long amount):
    cdef np.ndarray[long, ndim=1] output = np.zeros(shape=(amount,), dtype=long)
    for iteration in range(amount):
        output[iteration] = (randint(minV, maxV))
    return output

cpdef np.ndarray[long, ndim=1] bubble_Sort(np.ndarray input_data):
    cdef unsigned int i, j = 0
    cdef bint swapped = False
    cdef np.ndarray[long, ndim=1] data = input_data.copy()
    cdef unsigned short size = len(data)
    for j in range(size):
        swapped = False
        for i in range(0, size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break
    return data
