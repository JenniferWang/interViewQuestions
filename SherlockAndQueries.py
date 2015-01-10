import sys
def computeArrayA(A, B, C):
  modulo = 10**9 + 7
  min_B = min(B)
  max_B = max(B)
  cache = [1 for x in range(max_B - min_B + 1)]
  for i, val in enumerate(B):
    cache[val - min_B] = (cache[val - min_B] * C[i]) % modulo
  
  for i, val in enumerate(cache):
    curr = i + min_B - 1
    while curr < len(A):
      A[curr] = (A[curr] * val) % modulo
      curr += i + min_B
  print ' '.join(map(str, A))

def main():
  #g = sys.stdin
  g = open('SHERLOCK_TLE')
  #g = open('SHERLOCK')
  g.readline()
  str_A = g.readline().split()
  str_B = g.readline().split()
  str_C = g.readline().split()
  A = [int(x) for x in str_A]
  B = [int(x) for x in str_B]
  C = [int(x) for x in str_C]
  computeArrayA(A, B, C)

if __name__ == '__main__':
  main()
