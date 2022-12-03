def linear_search(number_list, number_to_find):
    for index, val in enumerate(number_list):
        if val == number_to_find:
            return index
    return -1


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

number_list = [12, 46, 78, 43, 965, 67, 35, 79]
sorted_list = sorted(number_list)
print(sorted_list)
number_to_find = 46

print(linear_search(number_list, number_to_find))
print(binary_search(sorted_list, number_to_find))