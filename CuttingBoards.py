import sys
def findMiniCosts(x_costs, y_costs, modulo):
  total_x_cuts = 1
  total_y_cuts = 1
  cost = 0
  x_costs.sort()
  y_costs.sort()
  pt_x = len(x_costs) - 1
  pt_y = len(y_costs) - 1
  while True:
    if pt_x == -1 and pt_y == -1:
      break
    if pt_x != -1 and (pt_y == -1 or x_costs[pt_x] > y_costs[pt_y]):
      cost = (cost + x_costs[pt_x] * total_y_cuts) % modulo
      pt_x -= 1
      total_x_cuts += 1
    else:
      cost = (cost + y_costs[pt_y] * total_x_cuts ) % modulo
      pt_y -= 1
      total_y_cuts += 1
  return cost

def main():
  #g = sys.stdin
  g = open('CUTTINGBOARDS')
  num_test = int(g.readline())
  modulo = 10 ** 9 + 7
  for _ in range(num_test):
    g.readline()
    x_costs = map(int, g.readline().split())
    y_costs = map(int, g.readline().split())
    print findMiniCosts(x_costs, y_costs, modulo)
    # ans:
    # 278642107
    # 951527138
    # 733709321
    # 159631732
    # 508889246
    # 288670782
    # 825619436
    # 604491628
    # 118087513
    # 134127017

if __name__ == '__main__':
  main()