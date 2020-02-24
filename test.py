from timeit import default_timer as timer
import gpu
import cpu
import testutil


# GENERATING
print("Generating data set 1000, NumPy: False")
start = timer()
data_small = cpu.generator(-1000, 1000, 1000, False)
time_gen_small = timer() - start

print("Generating data set 10000, NumPy: False")
start = timer()
data_big = cpu.generator(-10000, 10000, 10000, False)
time_gen_big = timer() - start

print("Generating data set 1000, NumPy: True")
start = timer()
data_np_small = cpu.generator(-1000, 1000, 1000, True)
time_gen_np_small = timer() - start

print("Generating data set 10000, NumPy: True")
start = timer()
data_np_big = cpu.generator(-10000, 10000, 10000, True)
time_gen_np_big = timer() - start


# SORTING GPU
start = timer()
print("Sorting with GPU 1000, NumPY: True")
new_output = gpu.bubble_Sort(data_np_small)
gpu_time_sort_np_small = timer() - start

start = timer()
print("Sorting with GPU 10000, NumPY: True")
new_output = gpu.bubble_Sort(data_np_big)
gpu_time_sort_np_big = timer() - start

start = timer()
print("Sorting with GPU 1000, NumPY: False")
new_output = gpu.bubble_Sort(data_small)
gpu_time_sort_small = timer() - start

start = timer()
print("Sorting with GPU 10000, NumPY: False")
new_output = gpu.bubble_Sort(data_big)
gpu_time_sort_big = timer() - start


# SORTING CPU
start = timer()
print("Sorting with CPU 1000,  NumPY: False")
new_output = cpu.bubble_Sort(data_small)
cpu_time_sort_small = timer() - start

start = timer()
print("Sorting with CPU 10000, NumPY: False")
new_output = cpu.bubble_Sort(data_big)
cpu_time_sort_big = timer() - start

start = timer()
print("Sorting with CPU 1000,  NumPY: True")
new_output = cpu.bubble_Sort(data_np_small)
cpu_time_sort_np_small = timer() - start

start = timer()
print("Sorting with CPU 10000, NumPY: True")
new_output = cpu.bubble_Sort(data_np_big)
cpu_time_sort_np_big = timer() - start


# SUMMARY GENERATING
testutil.clear()

print("Generating times:\n")

print("Small data set, Numpy: False\t{}".format(time_gen_small))
print("Big data set, Numpy: False\t{}".format(time_gen_big))
print("Small data set, Numpy: True\t{}".format(time_gen_np_small))
print("Big data set, Numpy: True\t{}".format(time_gen_np_big))
print("\n\n")


# SUMMARY GPU
print("Sorting with GPU:\n")

print("Small data set, Numpy: False\t{}".format(gpu_time_sort_small))
print("Big data set, Numpy: False\t{}".format(gpu_time_sort_big))
print("Small data set, Numpy: True\t{}".format(gpu_time_sort_np_small))
print("Big data set, Numpy: True\t{}".format(gpu_time_sort_np_big))
print("\n\n")


# SUMMARY CPU
print("Sorting with CPU:\n")

print("Small data set, Numpy: False\t{}".format(cpu_time_sort_small))
print("Big data set, Numpy: False\t{}".format(cpu_time_sort_big))
print("Small data set, Numpy: True\t{}".format(cpu_time_sort_np_small))
print("Big data set, Numpy: True\t{}".format(cpu_time_sort_np_big))
print("\n\n\n\n")
