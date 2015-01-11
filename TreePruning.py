# https://www.hackerrank.com/challenges/tree-pruning
import sys
class Tree:
  def __init__(self, weights):
    self.weights = weights
    self.n = len(weights)
    self.adj = [[] for x in range(self.n)]
    self.num_children = [0 for x in range(self.n)]
    self.dfsPrint = []
    self.dfsSeg = [0 for x in range(self.n)]

  def dfs(self, root):
    self.dfsPrint.append(root)
    self.dfsSeg[root] = 1
    for child in self.adj[root]:
      if self.dfsSeg[child] == 0:
        self.dfs(child)
        self.dfsSeg[root] += self.dfsSeg[child]
        
  def treePruning(self, k):
    self.dfs(0)
    pruned_w = [self.weights[0]]
    self.weightSum = [self.weights[0]]
    for l in range(1, self.n):
      pruned_w.append(pruned_w[-1] + self.weights[self.dfsPrint[l]])
    for _ in range(k):
      for i in range(self.n - 1, 0, -1): 
        pos = i + self.dfsSeg[self.dfsPrint[i]] - 1
        pruned_w[pos] = max(pruned_w[pos], pruned_w[i - 1])  
      for i in range(1, self.n):
        pruned_w[i] = max(pruned_w[i], pruned_w[i - 1] + self.weights[self.dfsPrint[i]])
    return pruned_w[-1]

def main():
  g = open('TREEPRUNING') #ans: 5656960015
  #g = sys.stdin
  [n, k] = map(int, g.readline().split())
  tree = Tree(map(int, g.readline().split()))
  for _ in range(n - 1):
    [u, v] = map(int, g.readline().split())
    tree.adj[u - 1].append(v - 1)
    tree.adj[v - 1].append(u - 1)
  print tree.treePruning(k)
  for i in range(n):
    print tree.dfsSeg[tree.dfsPrint[i]],

if __name__ == '__main__':
  main()