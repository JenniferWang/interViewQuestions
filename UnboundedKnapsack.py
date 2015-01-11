# https://www.hackerrank.com/challenges/unbounded-knapsack
import sys
class Knapsack:
  def __init__(self, loads):
    self.loads = loads
    self.cache = set(loads)

  def knapsack(self, target):
    dp = [False for x in range(target)]
    for i in range(len(dp)):
      for load in self.loads:
        if i + 1 == load or (i + 1 - load > 0 and dp[i - load]):
          dp[i] = True

    for i in range(len(dp) - 1, -1, -1):
      if dp[i]:
        return i + 1
    return 0
    
def main():
  g = sys.stdin
  #g = open('KNAPSACK')
  #ans:
  # 2000
  # 10
  # 2000
  # 1999
  num_tests = int(g.readline())
  for _ in range(num_tests):
    [n, target] = map(int, g.readline().split())
    loads = map(int, g.readline().split())
    sol = Knapsack(loads)
    print sol.knapsack(target)

if __name__ == '__main__':
  main()
