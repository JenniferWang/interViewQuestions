import sys
class Candy():
  def __init__(self):
    self.findMinSteps(1000)

  def findMinSteps(self, n):
    self.minSteps = [0]
    for i in range(1, n + 1):
      candidates = [self.minSteps[i - 1]]
      if i - 2 > -1:
        candidates.append(self.minSteps[i - 2])
      if i - 5 > -1:
        candidates.append(self.minSteps[i - 5])
      self.minSteps.append(min(candidates) + 1)

  def findMinOperation(self, initial):
    min_candy = min(initial)
    count = 0
    for candy in initial:
      if candy - min_candy > 0:
        count += self.minSteps[candy - min_candy]
    return count

def main():
  g = sys.stdin
  #g = open('EQUAL')
  num_tests = int(g.readline())
  candy = Candy()
  for _ in range(num_tests):
    g.readline()
    initial = map(int, g.readline().split())
    print candy.findMinOperation(initial)

if __name__ == '__main__':
  main()