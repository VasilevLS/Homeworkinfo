# # MergeSort
# # example based on: https://www.geeksforgeeks.org/python-program-for-merge-sort/
#
# def merge_sort(arr, l, r):
#     """
#     l is for left index and r is right index of the
#     sub-array of arr to be sorted
#     """
#     if l < r:
#         # Same as (l + r) // 2, but avoids overflow for large l
#         m = l + (r - l) // 2
#
#         # Sort first and second halves
#         merge_sort(arr, l, m)
#         merge_sort(arr, m + 1, r)
#         merge(arr, l, m, r)
#
#
# def merge(arr, l, m, r):
#     """
#     Merges two subarrays of arr[].
#     First subarray is arr[l..m]
#     Second subarray is arr[m+1..r]
#     """
#
#     # create temp arrays
#     L = arr[l:m + 1]
#     R = arr[m + 1:r + 1]
#
#     n1 = len(L)
#     n2 = len(R)
#
#     # Merge the temp arrays back into arr[l..r]
#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = l  # Initial index of merged subarray
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     if n1 < n2:
#         len_i = n2
#         list_i = R
#         idx_i = j
#     else:
#         len_i = n1
#         list_i = L
#         idx_i = i
#
#     while idx_i < len_i:
#         arr[k] = list_i[idx_i]
#         idx_i += 1
#         k += 1
#     '''
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#     '''
#
#
# # test
# arr = [9, 11, 13, 5, 6, 7]
# n = len(arr)
# print(f"Given: {arr}")
#
# merge_sort(arr, 0, n - 1)
# print(f"Sorted: {arr}")

# 1
# def is_min_heap(arr):
#     n = len(arr)
#     for i in range(n):
#         left = 2 * i + 1
#         right = 2 * i + 2
#
#         if left < n and arr[i] > arr[left]:
#             return 0
#         if right < n and arr[i] > arr[right]:
#             return 0
#     return 1
#
# arr = list(map(int, input().split()))
# print(is_min_heap(arr))
#
#
# 2
# f = input().split()
# pl = input().split()
# piano = input().split()
# res = []
# for i in pl:
#     if i in piano and i not in f:
#         res.append(int(i))
#
# print(*sorted(res))
#

# 3
#
# from collections import Counter
# def count_votes():
#     n = int(input().strip())
#     votes = []
#     for _ in range(n):
#         film = input().strip()
#         votes.append(film)
#     counter = Counter(votes)
#     sorted_films = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
#     for film, count in sorted_films:
#         print(f"{film} {count}")
#
#
# count_votes()

# 4
# import heapq
#
#
# def smallest_range(lists):
#     heap = []
#     max_val = float('-inf')
#     for i, lst in enumerate(lists):
#         heapq.heappush(heap, (lst[0], i, 0))
#         max_val = max(max_val, lst[0])
#     start, end = -10 ** 9, 10 ** 9
#     while heap:
#         min_val, list_idx, elem_idx = heapq.heappop(heap)
#         if max_val - min_val < end - start:
#             start, end = min_val, max_val
#         if elem_idx + 1 >= len(lists[list_idx]):
#             break
#         next_val = lists[list_idx][elem_idx + 1]
#         heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
#         max_val = max(max_val, next_val)
#     return f"{start}–{end}"
#
# n = int(input())
# lists = []
# for _ in range(n):
#     lists.append(list(map(int, input().split())))
#
# print(smallest_range(lists))


# 5
# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
#     return arr
#
#
# arr = list(map(int, input().split()))
# sorted_arr = heap_sort(arr)
# print(' '.join(map(str, sorted_arr)))


# 6
# def max_to_min_heap(arr):
#     def heapify_min(arr, n, i):
#         smallest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
# 
#         if left < n and arr[left] < arr[smallest]:
#             smallest = left
# 
#         if right < n and arr[right] < arr[smallest]:
#             smallest = right
# 
#         if smallest != i:
#             arr[i], arr[smallest] = arr[smallest], arr[i]
#             heapify_min(arr, n, smallest)
# 
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify_min(arr, n, i)
# 
#     return arr
# 
# 
# 
# max_heap = [9, 4, 7, 1, -2, 6] 
# min_heap = max_to_min_heap(max_heap.copy())
# print("Максимальная куча:", max_heap)
# print("Минимальная куча:", min_heap)
