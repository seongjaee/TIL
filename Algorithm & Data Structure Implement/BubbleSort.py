def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr)


bubble_sort([4, 2, 5, 7, 1, 3])
