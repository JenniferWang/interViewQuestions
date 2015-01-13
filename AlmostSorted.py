# https://www.hackerrank.com/challenges/almost-sorted
def isDescending(arr, a, b):
  for i in range(a + 1, b + 1):
    if arr[i] > arr[i - 1]:
      return False
  return True

def isAscending(arr, a, b):
  for i in range(a + 1, b + 1):
    if arr[i] < arr[i - 1]:
      return False
  return True

def isAlmostSorted(arr):
  n = len(arr)
  wrong_index = []
  left = 0
  while left < n - 1:
    if arr[left] > arr[left + 1]:
      break  
    left += 1
  if left == n - 1:
    print "yes"; return

  wrong1 = left
  right = len(arr) - 1
  while right > 0:
    if arr[right - 1] > arr[right]:
      break
    right -= 1
  wrong2 = right

  if wrong1 == wrong2:
     print 'no'; return

  arr[wrong1], arr[wrong2] = arr[wrong2], arr[wrong1]
  if isAscending(arr, wrong1, wrong2):
    if wrong1 > 0 and arr[wrong1] < arr[wrong1 - 1]:
      print 'no'; return
    if wrong2 < n - 1 and arr[wrong2] > arr[wrong2 + 1]:
      print 'no'; return
    print 'yes'
    print 'swap', wrong1 + 1, wrong2 + 1; return

  arr[wrong1], arr[wrong2] = arr[wrong2], arr[wrong1]
  if isDescending(arr, wrong1, wrong2):
    if wrong1 > 0 and arr[wrong2] < arr[wrong1 - 1]:
      print 'no'; return
    if wrong2 < n - 1 and arr[wrong1] > arr[wrong2 + 1]:
      print 'no'; return
    print 'yes'
    print 'reverse', wrong1 + 1, wrong2 + 1; return
  print 'no'; return

# isAlmostSorted([1, 2, 3])
# isAlmostSorted([1, 2, 3, 3])
# isAlmostSorted([1, 6, 2, 4, 5, 2])
# isAlmostSorted([1])
# isAlmostSorted([3, 1, 2])
# isAlmostSorted([4, 2])
isAlmostSorted([1, 5, 4, 3, 2, 6])
# g = sys.stdin
# g.readline()
# isAlmostSorted(map(int, g.readline().split()))