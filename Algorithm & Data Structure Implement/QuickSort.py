def quick_sort(arr):
    def sort(start, end):
        if end <= start:
            return
        pivot = partition(start, end)
        sort(start, pivot - 1)
        sort(pivot + 1, end)

    def partition(start, end):
        pivot_value = arr[start]
        left, right = start + 1, end

        while left <= right:
            while left <= right and arr[left] <= pivot_value:
                left += 1
            while left <= right and arr[right] >= pivot_value:
                right -= 1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]

        arr[start], arr[right] = arr[right], arr[start]
        return right

    sort(0, len(arr) - 1)


arr = [4, 1, 5, 3, 2, 7]
quick_sort(arr)
print(arr)
