import random
import time


def random_int_list(start=0, stop=100, length=10):
    return random.sample(range(start, stop), length)


def test_sort(array, fn_sort, show_result=True):
    if show_result:
        print("Before sorted: {}".format(array))
    start_time = time.time()
    fn_sort(array)
    end_time = time.time()
    if show_result:
        print("After sorted:  {}".format(array))
    print("Sort {0} done in {1:.5f} seconds".format(fn_sort.__name__, (end_time - start_time)))


def test_index_of(array, fn_index_of, key):
    start_time = time.time()
    index = fn_index_of(array, key)
    end_time = time.time()
    print("Search done in {0:.5f} seconds, index is {1}".format((end_time - start_time), index))


