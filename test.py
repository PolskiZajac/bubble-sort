from timeit import default_timer as timer
import sortnumba
import sortcython
import testutil


testutil.clear()

# GENERATING
print("Generating\t1000\tNumba")
start = timer()
data_numba_small = sortnumba.generator(-1000, 1000, 1000)
time_gen_numba_small = timer() - start

print("Generating\t10000\tNumba")
start = timer()
data_numba_big = sortnumba.generator(-10000, 10000, 10000)
time_gen_numba_big = timer() - start

print("Generating\t10000000\tNumba")
start = timer()
data_numba_large = sortnumba.generator(-10000000, 10000000, 10000000)
time_gen_numba_large = timer() - start


print("Generating\t1000\tCython")
start = timer()
data_cython_small = sortcython.generator(-1000, 1000, 1000)
time_gen_cython_small = timer() - start

print("Generating\t10000\tCython")
start = timer()
data_cython_big = sortcython.generator(-10000, 10000, 10000)
time_gen_cython_big = timer() - start

print("Generating\t10000000\tCython")
start = timer()
data_cython_large = sortcython.generator(-10000000, 10000000, 10000000)
time_gen_cython_large = timer() - start


# SORTING GPU
print("Sorting 1000 with\tNumba")
start = timer()
new_output = sortnumba.bubble_Sort(data_numba_small)
numba_time_sort_small = timer() - start

print("Sorting 10000 with\tNumba")
start = timer()
new_output = sortnumba.bubble_Sort(data_numba_big)
numba_time_sort_big = timer() - start


# SORTING CCPU
print("Sorting 1000 with\tCython")
start = timer()
new_output = sortcython.bubble_Sort(data_cython_small)
cython_time_sort_small = timer() - start

print("Sorting 10000 with\tCython")
start = timer()
new_output = sortcython.bubble_Sort(data_cython_big)
cython_time_sort_big = timer() - start

print("Sorting 10000000 with\tCython")
start = timer()
new_output = sortcython.bubble_Sort(data_cython_large)
cython_time_sort_large = timer() - start


# SUMMARY GENERATING
testutil.clear()

print("Generating times:\n")

print("Small data set,\tNumba\t{}".format(time_gen_numba_small))
print("Big data set,\tNumba\t{}".format(time_gen_numba_big))
print("Large data set,\tNumba\t{}".format(time_gen_numba_large))
print("\n")
print("Small data set,\tCython\t{}".format(time_gen_cython_small))
print("Big data set,\tCython\t{}".format(time_gen_cython_big))
print("Large data set,\tCython\t{}".format(time_gen_cython_large))
print("\n\n")


# SUMMARY Numba
print("Sorting with Numba:\n")

print("Small data set\t{}".format(numba_time_sort_small))
print("Big data set  \t{}".format(numba_time_sort_big))
print("\n\n")


# SUMMARY Cython
print("Sorting with Cython:\n")

print("Small data set\t{}".format(cython_time_sort_small))
print("Big data set  \t{}".format(cython_time_sort_big))
print("Large data set\t{}".format(cython_time_sort_large))
