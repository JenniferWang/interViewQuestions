import sys
def findMaximumSubarray(array):
  res1 = res2 = sum1 = array[0] 
  max_array = max(array)
  if max_array < 0:
    print str(max_array) + ' ' + str(max_array)
    return 
  for i in range(1, len(array)):
    res2 = max(array[i], res2 + array[i], res2)
    sum1 += array[i]
    res1 = max(sum1, res1)
    if sum1 < 0:
      sum1 = 0
  print str(res1) +' ' + str(res2)

def main():
  g = sys.stdin
  num_test = int(g.readline())
  for _ in range(num_test):
    g.readline()
    array = map(int, g.readline().split())
    findMaximumSubarray(array)

if __name__ == '__main__':
  main()
  