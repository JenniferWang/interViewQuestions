import sys
def findLongestCommonChild(A, B):
  n = len(A)
  pre = [0 for _ in range(n + 1)]
  for i in range(n):
    curr = [0]
    for j in range(n):
      if A[i] == B[j]:
        curr.append(1 + pre[j])
      else:
        curr.append(max(pre[j + 1], curr[j]))
    pre = curr
  return pre[-1]

#print findLongestCommonChild("HARRY", "SALLY")
def main():
  g = sys.stdin
  A = g.readline().strip()
  B = g.readline().strip()
  print findLongestCommonChild(A, B)

if __name__ == '__main__':
  main()
