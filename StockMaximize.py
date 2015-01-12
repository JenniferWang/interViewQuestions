import sys
def maximizeStockProfit(array):
  if len(array) == 0 or len(array) == 1:
    return 0
  profit = 0
  curr_max = array[-1]
  for i in xrange(len(array) - 1, -1, -1):
    if array[i] < curr_max:
      profit += curr_max - array[i]
    else:
      curr_max = array[i]
  return profit

def main():
  g = sys.stdin
  num_tests = int(g.readline())
  for _ in range(num_tests):
    g.readline()
    print maximizeStockProfit(map(int, g.readline().split()))

if __name__ == '__main__':
  main()


