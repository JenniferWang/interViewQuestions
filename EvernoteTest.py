def partition(arr, left, right):
  pt1, pt2 = left - 1, left
  while pt2 <= right:
    if arr[pt2] >= arr[right]:
      pt1 += 1
      arr[pt1], arr[pt2] = arr[pt2], arr[pt1]
    pt2 += 1
  return pt1

def quickSort(arr, left, right):
  pivot = partition(arr, left, right)
  if pivot - 1 > left:
    quickSort(arr, left, pivot - 1)
  if pivot + 1 < right:
    quickSort(arr, pivot + 1, right)

def find_K_QuickSort(arr, k):
  k = min(k, len(arr))
  left, right = 0, len(arr) - 1
  while left < right:
    pivot = partition(arr, left, right)
    if pivot == k:
      break
    if pivot < k:
      left = pivot + 1
    else:
      right = pivot - 1
  quickSort(arr, 0, k - 1)

  print arr[:k]
# arr = [5, 6]
# print find_K_QuickSort(arr, 2), arr
# arr = [5, 5 , 5, 6]
# print find_K_QuickSort(arr, 2), arr
# arr = [5, 5, 6, 6]
# print find_K_QuickSort(arr, 2), arr
arr = [54,26,93, 93, 17,77,93,31,44,55,20] #[93, 77, 55, 54, 44, 31, 26, 20, 17]
find_K_QuickSort(arr, 3)