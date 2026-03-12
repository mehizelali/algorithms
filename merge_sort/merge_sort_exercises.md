## Basics

### Exercise 1 – Trace by hand

Use merge sort to sort `[5, 2, 4, 7, 1, 3, 2, 6]`.

Write down:

- **The subarrays created at each recursive split**
- **The result of each merge step**

### Exercise 2 – Implement merge sort (array)

Write a function `merge_sort(arr)` that:

- **Recursively splits the array**
- **Merges sorted halves using a `merge(left, right)` helper**
- **Returns a new sorted list (do not sort in-place)**

### Exercise 3 – Count comparisons

Modify your `merge_sort` to count how many element comparisons (`<` or `<=`) are done while sorting an array.

- **Run it** on arrays of size 10, 100, 1000 (random values)
- **Compare your counts** to \(O(n \log n)\) behavior.

## Variations

### Exercise 4 – Sort in descending order

Adapt your merge sort to sort in **descending** order without changing too much of the code.

- **Question**: What minimal change is needed in the `merge` function?

### Exercise 5 – Stable vs unstable

Suppose you have an array of pairs `(value, id)` where `id` is a unique index.

- **Sort** by `value` using your merge sort.
- **Check** if equal `value`s keep their original input order – explain **why merge sort is stable** (or how to make it stable).

### Exercise 6 – Linked list merge sort

Given a singly linked list, implement `merge_sort_list(head)` using:

- **A function** to split a list into two halves (fast/slow pointers)
- **A merge function** for two sorted linked lists
- **No extra arrays allowed**, just re-link nodes.

## Thinking / Complexity

### Exercise 7 – Time and space complexity

- **Derive** the time complexity of merge sort using the recurrence \(T(n) = 2T(n/2) + O(n)\).
- **Analyze** the extra space complexity for:
  - **Array version**
  - **Linked list version**

### Exercise 8 – When is merge sort better than quicksort?

Answer in words and/or small examples:

- **Give 2 real situations** where merge sort is preferable to quicksort.
- **Give 2 situations** where merge sort is a bad choice.

### Exercise 9 – Count inversions using merge sort

An inversion is a pair \((i, j)\) with \(i < j\) and `a[i] > a[j]`.

- **Modify** merge sort to count the number of inversions in an array in \(O(n \log n)\).

