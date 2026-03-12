

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        hole = i
        # Shift elements to the right until we find the correct spot
        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value
    return arr

arr = [5, 2, 4, 7, 1, 3, 2, 6]
print(insertion_sort(arr))