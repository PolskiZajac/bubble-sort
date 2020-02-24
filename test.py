from timeit import default_timer as timer
import gpu
import ccpu
import testutil


# GENERATING
print("Generating data set 1000,  NumPy: False")
start = timer()
data_small = ccpu.generator(-1000, 1000, 1000)
time_gen_small = timer() - start

print("Generating data set 10000, NumPy: False")
start = timer()
data_big = ccpu.generator(-10000, 10000, 10000)
time_gen_big = timer() - start

print("Generating data set 1000,  NumPy: True")
start = timer()
data_np_small = gpu.generator(-1000, 1000, 1000, True)
time_gen_np_small = timer() - start

print("Generating data set 10000, NumPy: True")
start = timer()
data_np_big = gpu.generator(-10000, 10000, 10000, True)
time_gen_np_big = timer() - start


# # SORTING GPU
# print("Sorting with GPU 1000,  NumPY: True")
# start = timer()
# new_output = gpu.bubble_Sort(data_np_small)
# gpu_time_sort_np_small = timer() - start

# print("Sorting with GPU 10000, NumPY: True")
# start = timer()
# new_output = gpu.bubble_Sort(data_np_big)
# gpu_time_sort_np_big = timer() - start

# print("Sorting with GPU 1000,  NumPY: False")
# start = timer()
# new_output = gpu.bubble_Sort(data_small)
# gpu_time_sort_small = timer() - start

# print("Sorting with GPU 10000, NumPY: False")
# start = timer()
# new_output = gpu.bubble_Sort(data_big)
# gpu_time_sort_big = timer() - start


# SORTING CCPU
print("Sorting with CCPU 1000,  NumPY: False")
start = timer()
new_output = ccpu.bubble_Sort(data_small)
ccpu_time_sort_small = timer() - start

print("Sorting with CCPU 10000, NumPY: False")
start = timer()
new_output = ccpu.bubble_Sort(data_big)
ccpu_time_sort_big = timer() - start

print("Sorting with CCPU 1000,  NumPY: True")
start = timer()
new_output = ccpu.bubble_Sort(data_np_small)
ccpu_time_sort_np_small = timer() - start

# print("Sorting with CCPU 10000, NumPY: True")
# start = timer()
# new_output = ccpu.bubble_Sort(data_np_big)
# ccpu_time_sort_np_big = timer() - start

# SUMMARY GENERATING
testutil.clear()

print("Generating times:\n")

print("Small data set, Numpy: False\t{}".format(time_gen_small))
print("Big data set,   Numpy: False\t{}".format(time_gen_big))
# print("Small data set, Numpy: True\t{}".format(time_gen_np_small))
# print("Big data set,   Numpy: True\t{}".format(time_gen_np_big))
# print("\n\n")


# # SUMMARY GPU
# print("Sorting with GPU:\n")

# print("Small data set, Numpy: False\t{}".format(gpu_time_sort_small))
# print("Big data set,   Numpy: False\t{}".format(gpu_time_sort_big))
# print("Small data set, Numpy: True\t{}".format(gpu_time_sort_np_small))
# print("Big data set,   Numpy: True\t{}".format(gpu_time_sort_np_big))
print("\n\n")


# SUMMARY CCPU
print("Sorting with CCPU:\n")

print("Small data set, Numpy: False\t{}".format(ccpu_time_sort_small))
print("Big data set,   Numpy: False\t{}".format(ccpu_time_sort_big))
