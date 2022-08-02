def merge_sort(arr):
    if len(arr) == 1:
        return

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    print(f"left: {left_arr}, right: {right_arr}")

    merge_sort(left_arr)
    merge_sort(right_arr)

    left_i = 0
    right_i = 0
    arr_i = 0
    while left_i < len(left_arr) and right_i < len(right_arr):
        if left_arr[left_i] < right_arr[right_i]:
            arr[arr_i] = left_arr[left_i]
            left_i += 1
        else:
            arr[arr_i] = right_arr[right_i]
            right_i += 1
        arr_i += 1

    while left_i < len(left_arr):
        arr[arr_i] = left_arr[left_i]
        arr_i += 1
        left_i += 1

    while right_i < len(right_arr):
        arr[arr_i] = right_arr[right_i]
        arr_i += 1
        right_i += 1

    print(f"arr: {arr}")


arr = [4, 1, 5, 3, 2, 7]
merge_sort(arr)

print(arr)
