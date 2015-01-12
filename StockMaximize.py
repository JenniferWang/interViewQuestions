import sys
def maximizeStockProfit(array):
  if array == []:
    return 0
  if len(array) == 1:
    return 0
  max_index = array.index(max(array))
  profit = 0
  for i in range(max_index):
    profit += array[max_index] - array[i]
  return profit + maximizeStockProfit(array[max_index + 1:])
    
def main():
  g = sys.stdin
  num_tests = int(g.readline())
  for _ in range(num_tests):
    g.readline()
    print maximizeStockProfit(map(int, g.readline().split()))

if __name__ == '__main__':
  main()


