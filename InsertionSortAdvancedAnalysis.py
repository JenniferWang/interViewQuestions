# This is equivalent to count the inversion in an array
import sys
def countInversion(arr):
  n = len(arr)
  if n <= 1:
    return (arr[:], 0)
  leftArr, leftInv = countInversion(arr[: n/2])
  rightArr, rightInv = countInversion(arr[n/2 :])
  currInv = leftInv + rightInv
  mergedArr = []
  nl, nr = len(leftArr), len(rightArr)
  pl, pr = 0, 0
  while pl < nl and pr < nr:
    if leftArr[pl] <= rightArr[pr]:
      mergedArr.append(leftArr[pl])
      pl += 1
    else:
      mergedArr.append(rightArr[pr])
      pr += 1
      currInv += nl - pl
  if pl < nl:
    mergedArr += leftArr[pl :]
  elif pr < nr:
    mergedArr += rightArr[pr :]
  return (mergedArr, currInv)

# print countInversion([2,1,3,1,2])
def main():
  g = sys.stdin
  num_tests = int(g.readline())
  for _ in range(num_tests):
    g.readline()
    print countInversion(map(int, g.readline().split()))[1]

if __name__ == "__main__":
  main()








