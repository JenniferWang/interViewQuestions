import sys
def computeArrayA(A, B, C):
  modulo = 10**9 + 7
  cache = {}
  for i in range(len(B)):
    val = B[i]% modulo
    if val in cache:
      cache[val] *= C[i]
    else:
      cache[val] = C[i]

  for key in cache:
    curr = key - 1
    while curr < len(A):
      A[curr] = (A[curr] * cache[key]) % modulo
      curr += key
  print ' '.join(map(str, A))

def main():
  g = sys.stdin
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
