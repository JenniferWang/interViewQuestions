# https://www.hackerrank.com/challenges/sherlock-and-minimax
import sys
class MiniMax:
  def updateMinGap(self, val):
    curr_gap = min([abs(x - val) for x in self.array]) 
    if curr_gap > self.min_gap:
      self.min_gap = curr_gap
      self.res = val

  def findMiniMax(self,array, P, Q):
    array = list(set(array))
    array.sort()
    self.array = array
    self.min_gap = 0
    self.res = array[0]

    self.updateMinGap(P)
    for i in range(1, len(array)):
      val_candidates = [(array[i] + array[i - 1])/ 2, \
        (array[i] + array[i - 1] + 1)/ 2]
      for val in val_candidates:
        if val > P and val < Q:
          self.updateMinGap(val)
    self.updateMinGap(Q)
    return self.res

def main():
  #g = sys.stdin
  g = open("SHERLOCKMINIMAX") # ans: 16
  g.readline()
  array = map(int, g.readline().split())
  [P, Q] = map(int, g.readline().split())
  sol = MiniMax()
  print sol.findMiniMax(array, P, Q)

if __name__ == '__main__':
  main()