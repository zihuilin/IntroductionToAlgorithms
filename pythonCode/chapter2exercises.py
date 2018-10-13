import pythonCode.common as common


def insert_sort(array=[], is_desc=True):  # 2.1-2
    for index_to_sort in range(1, len(array)):
        key = array[index_to_sort]
        current_index = index_to_sort - 1
        while current_index >= 0:
            test = array[current_index] > key if is_desc else array[current_index] < key
            if test:
                break
            array[current_index + 1] = array[current_index]
            current_index = current_index - 1
        array[current_index + 1] = key


def run_exercise2_1_2():
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        insert_sort(array, True)
    common.test_sort(array_to_be_sorted, fn_sort, True)


def find_index(array, element):  # 2.1-3
    index = 0
    while index < len(array) and array[index] != element:
        index = index + 1
    return index if index != len(array) else None


def run_exercise2_1_3():
    array = [1, 3, 5, 7, 9]
    print(find_index(array, 1))
    print(find_index(array, 9))
    print(find_index(array, 2))


def add_binary_array(array1, array2):  # 2.1-4
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


def run_exercise2_1_4():
    array1 = [1, 0, 1, 0]
    array2 = [1, 1, 0, 1]
    result = add_binary_array(array1, array2)
    print(result)


def select_sort(array, is_desc):
    for select_index in range(len(array) - 1):  # last element don't need to be selected
        target_index = select_index
        min_or_max_index = target_index
        target_index = target_index + 1
        while target_index < len(array):
            if is_desc:
                if array[target_index] < array[min_or_max_index]:
                    temp = array[target_index]
                    array[target_index] = array[min_or_max_index]
                    array[min_or_max_index] = temp
            elif array[target_index] > array[min_or_max_index]:
                temp = array[target_index]
                array[target_index] = array[min_or_max_index]
                array[min_or_max_index] = temp
            target_index = target_index + 1


def run_exercise2_2_2():
    array_to_be_sorted = common.random_int_list()

    def fn_sort(array):
        select_sort(array, True)
    common.test_sort(array_to_be_sorted, fn_sort, True)


if __name__ == '__main__':
    # run_exercise2_1_2()
    # run_exercise2_1_3()
    # run_exercise2_1_4()
    run_exercise2_2_2()

