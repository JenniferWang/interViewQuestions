import sys
def findLongestCommonSubsequence(A, B):
  n = len(A)
  m = len(B)
  i = 1
  while i <= m:
    if A[0] == B[i - 1]:
      break
    i += 1
  pre = [[]] * (i - 1) + [[A[0]]] * (m - i + 1)

  for i in range(1, n):
    curr = [[] for _ in range(m)]
    for j in range(m):
      if A[i] == B[j]:
        if j == 0:
          curr[j].append(A[i])
        else:
          curr[j] = pre[j - 1] + [A[i]]
      else:
        curr[j] = pre[j][:]
        if j > 0 and len(curr[j - 1]) > len(curr[j]):
          curr[j] = curr[j - 1]
    pre = curr
  return ' '.join(map(str, pre[-1]))

def main():
  g = sys.stdin
  #g = open("LCS_2")
  g.readline()
  A = map(int, g.readline().split())
  B = map(int, g.readline().split())
  print findLongestCommonSubsequence(A, B)

if __name__ == "__main__":
  main()

