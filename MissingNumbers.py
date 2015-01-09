import sys
def findMissingNumbers(A, B):
  min_B = min(B)
  max_B = max(B)
  buckets = [0 for x in range(max_B - min_B + 1)]
  for val in B:
    buckets[val - min_B] += 1
  for val in A:
    buckets[val - min_B] -= 1
  res = []
  for index, val in enumerate(buckets):
    if val != 0:
      res.append(index + min_B)
  print ' '.join(map(str, res))

def main():
  g = sys.stdin
  g.readline()
  A = map(int, g.readline().split())
  g.readline()
  B = map(int, g.readline().split())
  findMissingNumbers(A, B)

if __name__ == '__main__':
  main()
