#https://www.hackerrank.com/challenges/play-game
import sys
def findMaxScore(bricks):
  """
  For p1, he can take 1, 2, or 3 steps
  if take 1 step:
    optimalScore[0: n] = bricks[:1] + (sum(bricks[1:]) - optimalScore[1: n])
  if take 2 steps:
    optimalScore[0: n] = bricks[:2] + (sum(bricks[2:]) - optimalScore[2: n])
  if take 3 steps:
    optimalScore[0: n] = bricks[:3] + (sum(bricks[3:]) - optimalScore[3: n])
  Thus, we scan from the end of the bricks
  """
  n = len(bricks)
  if n <= 3:
    return sum(bricks)
  maxScore = [sum(bricks[n - 3:]), sum(bricks[n - 2:]), bricks[-1]]
  sumFromEnd = maxScore[0]
  for i in range(n - 4, -1, -1):
    curr = bricks[i] + sumFromEnd - min(maxScore)
    maxScore.pop()
    maxScore.insert(0, curr)
    sumFromEnd += bricks[i]
  return maxScore[0]

#print findMaxScore([0, 1, 1, 1, 999]) # = 999
def main():
  g = sys.stdin
  num_tests = int(g.readline())
  for _ in range(num_tests):
    g.readline()
    print findMaxScore(map(int, g.readline().split()))

if __name__ == '__main__':
  main()




