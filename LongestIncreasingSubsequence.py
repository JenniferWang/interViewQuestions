import sys
def main():
  #g = sys.stdin
  g = open('LIS')
  length = int(g.readline())
  tailTable = []
  for _ in range(length):
    val = int(g.readline())
    if not tailTable or val > tailTable[-1]:
      tailTable.append(val)
    else:
      if val < tailTable[0]:
        tailTable[0] = val
      else:
        left = -1
        right = len(tailTable) - 1
        while right - left > 1:
          middle = (right + left) / 2
          if tailTable[middle] >= val:
            right = middle
          else:
            left = middle
        tailTable[right] = val
  print len(tailTable)

if __name__ == '__main__':
  main()
