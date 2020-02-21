input_data = [2, 3, 5, 1, 0, 6, 8, 9, 7, 4]
output_data = []


def bubbleSort(data):
    size = len(data)
    i = j = t = 0
    while i < size - 1:
        while j < size - 1:
            if data[j] > data[j + 1]:
                t = data[j]
                data[j] = data[j + 1]
                data[j + 1] = t
            j += 1
        i += 1
    return data


output_data = bubbleSort(input_data)
print(output_data)
