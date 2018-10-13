import Python.common as common


def insert_sort(array):  # P25, 中文版14页
    for current in range(1, len(array)):
        key = array[current]
        temp_index = current - 1
        while temp_index >= 0 and array[temp_index] > key:
            array[temp_index + 1] = array[temp_index]
            temp_index = temp_index - 1
        array[temp_index + 1] = key


def _merge(array, p, q, r):  # P30, 中文版17页
    array_left_len = q - p + 1
    array_right_len = r - q
    array_left = []
    array_right = []
    for index in range(array_left_len):
        array_left.append(array[p + index])
    for index in range(array_right_len):
        array_right.append(array[q + 1 + index])
    array_left.append(float('inf'))
    array_right.append(float('inf'))
    index_left = 0
    index_right = 0
    for index in range(p, r + 1):
        if array_left[index_left] < array_right[index_right]:
            array[index] = array_left[index_left]
            index_left = index_left + 1
        else:
            array[index] = array_right[index_right]
            index_right = index_right + 1


def merge_sort(array, p, r):  # P31, 中文版19页
    if p < r:
        q = int((r+p)/2)
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        _merge(array, p, q, r)


if __name__ == '__main__':
    array_to_sort = common.random_int_list(1, 100000, 10000)
    common.test_sort(list(array_to_sort), insert_sort)

    def fn_merge_sort(array):
        merge_sort(array, 0, len(array) - 1)

    common.test_sort(list(array_to_sort), fn_merge_sort)

    # array_to_merge = [1,3,5,7,2,4,6,8]
    # _merge(array_to_merge,0,3,7)
    # print(array_to_merge)





