#Given a m * n matrix, find the number of balanced number in the matrix
#definition: a number A[i][j] is balanced, if
# sum(A[i][:j]) == sum(A[i][j + 1:]) == sum(A[:i][j]) == sum(A[i + 1:][j])
def findBalancedNumber(matrix):
  if matrix == [[]]:
    return 0
  m = len(matrix)
  n = len(matrix[0])
  row_sum = [(0, sum(matrix[i][1:])) for i in range(m)]
  col_sum = [(0, sum([matrix[i][j] for i in range(1, m)])) for j in range(n)]
  #print row_sum, col_sum
  res = 0
  for i in range(m):
    for j in range(n):
      left, right = row_sum[i]
      up, down = col_sum[j]
      if left == right and right == up and up == down:
        res += 1
      if j + 1 < n:
        row_sum[i] = (left + matrix[i][j], right - matrix[i][j + 1])
      else:
        row_sum[i] = (left + matrix[i][j], 0)
      if i + 1 < m:
        col_sum[j] = (up + matrix[i][j], down - matrix[i + 1][j])
      else:
        col_sum[j] = (up + matrix[i][j], 0)
  return res

print findBalancedNumber([[0]]) == 1
print findBalancedNumber([[1]]) == 1
print findBalancedNumber([[0], [0]]) == 2
print findBalancedNumber([[0, 1]]) == 1
print findBalancedNumber([[0, 0]]) == 2
print findBalancedNumber([[0, 2], [1, 0]]) == 2
print findBalancedNumber([[1, 1],[1, 1]]) == 0
print findBalancedNumber([[1, 1, 1],[1, 1, 1], [1, 1, 1]]) == 1
