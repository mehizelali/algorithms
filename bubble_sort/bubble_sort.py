

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


arr = [5, 2, 4, 7, 1, 3, 2, 6]
print(bubble_sort(arr))
            

