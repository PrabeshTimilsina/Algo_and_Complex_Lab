def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        m = i
        for j in range(i + 1, size):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]

    return arr


