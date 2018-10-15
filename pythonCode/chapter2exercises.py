import pythonCode.common as common


def insert_sort_e2_1_2(array=[], is_desc=True):  # 2.1-2
    for index_to_sort in range(1, len(array)):
        key = array[index_to_sort]
        current_index = index_to_sort - 1
        while current_index >= 0:
            if (is_desc and array[current_index] > key) or \
                    (not is_desc and array[current_index] < key):
                break
            array[current_index + 1] = array[current_index]
            current_index = current_index - 1
        array[current_index + 1] = key


def run_exercise2_1_2():
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        insert_sort_e2_1_2(array, True)
    common.test_sort(array_to_be_sorted, fn_sort)


def find_index_e2_1_3(array, element):  # 2.1-3
    index = 0
    while index < len(array) and array[index] != element:
        index = index + 1
    return index if index != len(array) else None


def run_exercise2_1_3():
    array = [1, 3, 5, 7, 9]
    print(find_index_e2_1_3(array, 1))
    print(find_index_e2_1_3(array, 9))
    print(find_index_e2_1_3(array, 2))


def add_binary_array_e2_1_4(array1, array2):  # 2.1-4
    result_array = [0] * (len(array1) + 1)
    carry = 0
    for index in range(len(array1) - 1, -1, -1):
        if array1[index] and array2[index]:
            if carry:
                result_array[index + 1] = 1
            else:
                result_array[index + 1] = 0
            carry = 1
        elif array1[index] or array2[index]:
            if carry:
                result_array[index + 1] = 0
                carry = 1
            else:
                result_array[index + 1] = 1
                carry = 0
        else:
            if carry:
                result_array[index + 1] = 1
            else:
                result_array[index + 1] = 0
            carry = 0
    if carry:
        result_array[0] = 1
    else:
        result_array[0] = 0
    return result_array


def run_exercise2_1_4():  # 2.2-2
    array1 = [1, 0, 1, 0]
    array2 = [1, 1, 0, 1]
    result = add_binary_array_e2_1_4(array1, array2)
    print(result)


def select_sort_e2_2_2(array, is_desc):
    for select_index in range(len(array) - 1):  # last element don't need to be selected
        target_index = select_index
        min_or_max_index = target_index
        target_index = target_index + 1
        while target_index < len(array):
            if (is_desc and array[target_index] < array[min_or_max_index]) or \
                    (not is_desc and array[target_index] > array[min_or_max_index]):
                temp = array[target_index]
                array[target_index] = array[min_or_max_index]
                array[min_or_max_index] = temp
            target_index = target_index + 1


def run_exercise2_2_2():
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        select_sort_e2_2_2(array, False)
    common.test_sort(array_to_be_sorted, fn_sort)


def merge_e2_3_2(array, p, q ,r):
    array_left_len = q - p + 1
    array_right_len = r - q
    array_left = array[p:q+1]
    array_right = array[q+1:r+1]
    index_left = 0
    index_right = 0

    for merge_index in range(p, r+1):
        if index_left < array_left_len and index_right == array_right_len:
            array[merge_index] = array_left[index_left]
            index_left = index_left + 1
            continue
        if index_right < array_right_len and index_left == array_left_len:
            array[merge_index] = array_right[index_right]
            index_right = index_right + 1
            continue
        if array_left[index_left] < array_right[index_right]:
            array[merge_index] = array_left[index_left]
            index_left = index_left + 1
        else:
            array[merge_index] = array_right[index_right]
            index_right = index_right + 1


def merge_sort_e2_3_2(array, p, r):
    if p < r:
        q = int((r + p) / 2)
        merge_sort_e2_3_2(array, p, q)
        merge_sort_e2_3_2(array, q + 1, r)
        merge_e2_3_2(array, p, q, r)


def run_exercise_2_3_2():
    array = common.random_int_list()

    def fn_sort(array):
        merge_sort_e2_3_2(array, 0, len(array)-1)
    common.test_sort(array, fn_sort)


def insert_sort_recursive_e2_3_4(array, n, is_desc):
    if n > 0:
        insert_sort_recursive_e2_3_4(array, n-1, is_desc)
    key = array[n]
    index = n - 1
    while index >= 0:
        if (is_desc and array[index] <= key) or \
                (not is_desc and array[index] >= key):
            break
        array[index + 1] = array[index]
        index = index - 1
    array[index + 1] = key


def run_exercise_2_3_4():
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        insert_sort_recursive_e2_3_4(array_to_be_sorted, len(array) - 1, True)
    common.test_sort(array_to_be_sorted, fn_sort)


if __name__ == '__main__':
    # run_exercise2_1_2()
    # run_exercise2_1_3()
    # run_exercise2_1_4()
    # run_exercise2_2_2()
    # run_exercise_2_3_2()
    run_exercise_2_3_4()

