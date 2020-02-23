from random import randint
from timeit import default_timer as timer
import numpy as np
from numba import cuda, jit


def generator(minV, maxV, amount, numpy=True):
    output = []
    for iterate in range(0, amount, 1):
        output.append(randint(minV, maxV))
    if numpy is True:
        np_output = np.array(output)
        return np_output
    else:
        return output


@jit(nopython=True)
def bubble_Sort(input_data):
    number = swaps = i = j = t = 0
    swapped = False

    data = input_data.copy()
    size = len(data)

    for j in range(size):
        swapped = False

        for i in range(0, size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

    return data


print("Generating")
new_data = generator(-1000, 1000, 1000, True)
start = timer()
print("Sorting")
new_output = bubble_Sort(new_data)
print("Time:", timer()-start)
