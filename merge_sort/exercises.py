"""
Exercise 1 – Trace by hand
Use merge sort to sort [5, 2, 4, 7, 1, 3, 2, 6].

Write down:

The subarrays created at each recursive split
The result of each merge step
"""


# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr 
    
#     mid = len(arr) // 2 

#     left = merge_sort(arr[:mid])
    
#     right = merge_sort(arr[mid:])
#     print('left', left, "right", right)
#     return merge(left, right)
    



# def merge(left, right):

#     results = []

#     i = j = 0

#     while i <  len(left) and j < len(right):
#         if left[i] <= right[j]:
#             results.append(left[i])
#             i += 1
#         else: 
#             results.append(right[j])
#             j += 1


#     results.extend(left[i:])
#     results.extend(right[j:])
#     return results


# arr = [5, 2, 4, 7, 1, 3, 2, 6]


# print(merge_sort(arr))


"""
Exercise 3 – Count comparisons
Modify your merge_sort to count how many element comparisons (< or <=) are done while sorting an array.

Run it on arrays of size 10, 100, 1000 (random values)
Compare your counts to (O(n \log n)) behavior.

"""




# import random

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return 0, arr

#     mid = len(arr) // 2

#     left_count, left = merge_sort(arr[:mid])
#     right_count, right = merge_sort(arr[mid:])

#     merge_count, merged = merge(left, right)
#     print(merge_count)
#     return left_count + right_count + merge_count, merged


# def merge(left, right):
#     i = j = 0
#     comparisons = 0
#     result = []

#     while i < len(left) and j < len(right):
#         comparisons += 1
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return comparisons, result


# sizes = [10, 100, 1000]
# arr = [5, 2, 4, 7, 1, 3, 2, 6]


# print(merge_sort(arr))
# for n in sizes:
#     arr = [random.randint(0, 10000) for _ in range(n)]
#     comparisons, sorted_arr = merge_sort(arr)

#     print(f"n = {n}")
#     print(f"comparisons = {comparisons}")
#     print(f"n log2(n) ≈ {int(n * (n.bit_length()-1))}")
#     print()

"""
Exercise 4 – Sort in descending order
Adapt your merge sort to sort in descending order without changing too much of the code.

Question: What minimal change is needed in the merge function?
"""


"""
Exercise 5 – Stable vs unstable
Suppose you have an array of pairs (value, id) where id is a unique index.

Sort by value using your merge sort.
Check if equal values keep their original input order – explain why merge sort is stable (or how to make it stable).
"""