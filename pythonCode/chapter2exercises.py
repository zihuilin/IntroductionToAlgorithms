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


if __name__ == '__main__':
    # run_exercise2_1_2()
    run_exercise2_1_3()
