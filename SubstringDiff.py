# https://www.hackerrank.com/challenges/substring-diff/forum
# A not bad problem
import sys
def _help_findMaxPossibleLength(S, P, Q):
  n = len(P)
  maxLength = S
  for i in range(n):
    pt_P = 0
    pt_Q = i
    pre_start = i
    mis_index = []
    misCount = 0
    while pt_Q < n: 
      if P[pt_P] != Q[pt_Q]:
        misCount += 1
        mis_index.append(pt_Q)
        if misCount == S + 1:
          misCount -= 1
          maxLength = max(maxLength, pt_Q - pre_start)
          pre_start = mis_index[- (S + 1)] + 1
      pt_P += 1
      pt_Q += 1
    maxLength = max(maxLength, n - pre_start)
  return maxLength

def findMaxPossibleLength(S, P, Q):
  return max(_help_findMaxPossibleLength(S, P, Q), _help_findMaxPossibleLength(S, Q, P))
#print findMaxPossibleLength(0, 't','b')
print findMaxPossibleLength(2, 'torino', 'tabriz') # 4
print findMaxPossibleLength(2, "tabriz", "torino")
#print findMaxPossibleLength(0, 'abacba', 'abcaba')# 3
#print findMaxPossibleLength(3, 'helloworld', 'yellomarin') # 8

def main():
  g = sys.stdin
  num_tests = int(g.readline())
  for _ in range(num_tests):
    line =  g.readline().split()
    print findMaxPossibleLength(int(line[0]), line[1], line[2])

# if __name__ == "__main__":
#   main()