import sys

def countSimilarPairs(tree_array, T):
  count = 0
  for i in xrange(len(tree_array)):
    if i == tree_array[i]:
      continue
    parent = tree_array[i]
    while True:
      if abs(i - parent) <= T:
        count += 1
      if parent == tree_array[parent]:
        break
      parent = tree_array[parent]
  print count

def main():
  g = sys.stdin
  #g = open("SIMILARPAIR") #OUTPUT: 4058469201
  firstLine = g.readline().split()
  num_nodes = int(firstLine[0])
  T = int(firstLine[1])
  tree_array = [x for x in range(num_nodes)]
  for line in g:
    [father, child] = map(int, line.split())
    tree_array[child - 1] = father - 1
  countSimilarPairs(tree_array, T)

if __name__ == '__main__':
  main()

