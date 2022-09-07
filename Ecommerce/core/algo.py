def selection_sort(arr):
    for i in range(0, len(arr)-1):
        curr_min_idx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[curr_min_idx]:
                curr_min_idx = j

        arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]

arr = [3, 2, 6, 4, 1, 5]

selection_sort(arr)
print(arr)
