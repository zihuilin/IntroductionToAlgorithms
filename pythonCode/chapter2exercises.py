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
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        merge_sort_e2_3_2(array, 0, len(array)-1)
    common.test_sort(array_to_be_sorted, fn_sort)


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


def binary_search_iteration_e2_3_5(array, key):
    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        check_index = int((start_index + end_index)/2)
        if key == array[check_index]:
            return check_index
        elif key > array[check_index]:
            start_index = check_index + 1
        else:
            end_index = check_index - 1
    return None


def binary_search_recursive_e2_3_5(array, start_index, end_index, key):
    if start_index > end_index:
        return None
    check_index = int((start_index + end_index) / 2)
    if key == array[check_index]:
        return check_index
    elif key > array[check_index]:
        return binary_search_recursive_e2_3_5(array, check_index + 1, end_index, key)
    else:
        return binary_search_recursive_e2_3_5(array, start_index, check_index - 1, key)


def run_exercise_2_3_5():
    array_to_be_searched = [1, 2, 3, 4, 5]
    key_to_be_searched = 2
    common.test_index_of(array_to_be_searched, binary_search_iteration_e2_3_5, key_to_be_searched)

    def fn_search(array, key):
        return binary_search_recursive_e2_3_5(array, 0, len(array)-1, key)
    common.test_index_of(array_to_be_searched, fn_search, key_to_be_searched)


def insert_sort_with_binary_search_e2_3_6(array):
    current_index = 1
    while current_index < len(array):
        key = array[current_index]
        start_index = 0
        end_index = current_index - 1
        check_index = int((start_index + end_index) / 2)
        while start_index < end_index:
            if key == array[check_index]:
                break
            elif key > array[check_index]:
                start_index = check_index + 1
                check_index = int((start_index + end_index) / 2)
            else:
                end_index = check_index - 1
                check_index = int((start_index + end_index) / 2)
        index = current_index - 1
        while index >= check_index:
            array[index + 1] = array[index]
            index = index - 1
        array[check_index + 1] = key
        current_index = current_index + 1


def run_exercise_2_3_6():
    array_to_sort = range(10000, 1, -1)
    # array_to_sort = range(1, 10000, 1)
    # array_to_sort = common.random_int_list(1, 100000, 10000)
    common.test_sort(list(array_to_sort), insert_sort_with_binary_search_e2_3_6, False)

    def fn_merge_sort(array):
        merge_sort_e2_3_2(array, 0, len(array) - 1)

    common.test_sort(list(array_to_sort), fn_merge_sort, False)


def merge_e2_3_7(array, p, q, r):
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
        if array_left[index_left] == array_right[index_right]:
            return True
        if array_left[index_left] < array_right[index_right]:
            array[index] = array_left[index_left]
            index_left = index_left + 1
        else:
            array[index] = array_right[index_right]
            index_right = index_right + 1
    return False


def merge_sort_as_find_same_elements(array, p, r):
    if p < r:
        q = int((r+p)/2)
        has_same_elements = merge_sort_as_find_same_elements(array, p, q)
        has_same_elements = merge_sort_as_find_same_elements(array, q+1, r)
        has_same_elements = merge_e2_3_7(array, p, q, r)
        if has_same_elements:
            return True
    return False


def run_exercise_2_3_7():
    array_to_search = common.random_int_list(1, 100000, 10000)
    # array_to_search.append(array_to_search[300])
    has_same_elements = merge_sort_as_find_same_elements(array_to_search, 0, len(array_to_search)-1)
    print(has_same_elements)


if __name__ == '__main__':
    # run_exercise2_1_2()
    # run_exercise2_1_3()
    # run_exercise2_1_4()
    # run_exercise2_2_2()
    # run_exercise_2_3_2()
    # run_exercise_2_3_4()
    # run_exercise_2_3_5()
    # run_exercise_2_3_6()
    run_exercise_2_3_7()

