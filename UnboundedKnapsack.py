# https://www.hackerrank.com/challenges/unbounded-knapsack
import sys
class Knapsack:
  def __init__(self, loads):
    self.loads = loads
    self.cache = set(loads)

  def memo(self, target):
    if target in self.cache:
      return True
    for load in self.loads:
      if target - load > 0 and self.memo(target - load):
        self.cache.add(target)
        return True
    return False

  def knapsack(self, target):
    if target < min(self.loads):
      return 0
    for t in range(target, -1, -1):
      if self.memo(t):
        return t
    return 0

def main():
  #g = sys.stdin
  g = open('KNAPSACK')
  num_tests = int(g.readline())
  for _ in range(num_tests):
    [n, target] = map(int, g.readline().split())
    loads = map(int, g.readline().split())
    sol = Knapsack(loads)
    print sol.knapsack(target)

if __name__ == '__main__':
  main()
