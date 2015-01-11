import sys
class Words:
  def __init__(self, words):
    self.s = words
    self.n = len(words)
    self.forwardArray = [None for x in range(self.n)]
    self.backwardArray = [None for x in range(self.n)]

  def buildPalindromeArray(self):
    self.forwardArray[0] = 1
    self.backwardArray[-1] = 1
    pre_0 = [0 for x in range(self.n)]
    pre_1 = [1 for x in range(self.n)]
    for length in range(1, self.n):
      curr = []
      for left in range(self.n - length):
        if self.s[left] == self.s[left + length]:
          curr.append(pre_0[left + 1] + 2)
        else:
          curr.append(max(pre_1[left], pre_1[left + 1]))
      
      self.forwardArray[length] = curr[0]
      self.backwardArray[self.n - length - 1] = curr[-1]
      pre_0, pre_1 = pre_1, curr

  def findMaxScore(self):
    self.buildPalindromeArray()
    if self.n < 2:
      return 0
    score = 0
    for i in range(1, self.n - 1):
      score = max(score, self.forwardArray[i - 1] * self.backwardArray[i])
    return score

def main():
  g = sys.stdin
  #g = open('PLAYWITHWORDS')
  words = g.readline()
  w = Words(words)
  print w.findMaxScore()

if __name__ == '__main__':
  main()

