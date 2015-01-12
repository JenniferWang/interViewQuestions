import sys
class Candy():
  def __init__(self, initial):
    self._initial = initial

  def _findMinSteps(self, n):
    n1 = n % 5
    n2 = n1 % 2
    return n / 5 + n1 / 2 + n2

  def _findMinOperationToResult(self, result):
    return sum([self._findMinSteps(num - result) for num in self._initial])

  def findMinOperation(self):
    min_candy = min(self._initial)
    operations = [
      self._findMinOperationToResult(result) 
      for result in xrange(min_candy - 4, min_candy + 1)
    ]
    return min(operations)

def main():
  # g = sys.stdin
  g = open('EQUAL')
  num_tests = int(g.readline())
  for _ in range(num_tests):
    g.readline()
    initial = map(int, g.readline().split())
    print Candy(initial).findMinOperation()

if __name__ == '__main__':
  main()
