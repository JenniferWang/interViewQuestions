# https://www.hackerrank.com/challenges/red-john-is-back
import sys
class Configuration():
  def __init__(self):
    self.cache = {0: 1, 1:1, 2: 1, 3: 1}

  def countConfiguration(self, N):
    if N in self.cache:
      return self.cache[N]
    if N - 4 >= 0:
      return self.countConfiguration(N - 1) + self.countConfiguration(N - 4)
    else:
      return self.countConfiguration(N - 1)

class Prime():
  def __init__(self):
    self.isPrime = []
  
  def countPrime(self, N):
    if len(self.isPrime) >= N:
      return sum(self.isPrime[:N]) - 1
    pre_result = len(self.isPrime)
    self.isPrime = self.isPrime + [1] * (N - len(self.isPrime))
    for i in range(1, N):
      val = i + 1
      curr = val * 2 - 1
      while curr < N:
        self.isPrime[curr] = 0
        curr += val
    return sum(self.isPrime[: N]) - 1

def main():
  g = sys.stdin
  #g = open('RED')
  num_tests = int(g.readline())
  conf = Configuration()
  prime = Prime()
  for _ in range(num_tests):
    n = int(g.readline())
    numConfig = conf.countConfiguration(n)
    print n, numConfig
    print prime.countPrime(numConfig)


if __name__ == '__main__':
  main()

