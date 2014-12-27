# No.12 calculate 1 + 2 + ... + n without * or / or for, else, if, switch, case ...
# Use class static variable
# http://blog.sina.com.cn/s/blog_8d581f830100xxfk.html
# http://blog.csdn.net/shiren_bod/article/details/6703467
class Sum:
  summation = 0
  count = 0
  def __init__(self):
    Sum.count += 1
    Sum.summation += Sum.count

def getSum(n):
  [Sum()] * n # if we use C++ here, we won't have this * 
  print Sum.summation

getSum(1)
getSum(2)
getSum(3)

def recursion(summ, n):
  n and recursion(summ, n - 1) # use n = 0 to end the recursion
  summ[0] += n

def getSumRecursion(n):
  summ = [0]
  recursion(summ, n)
  print summ[0]

getSumRecursion(1)
getSumRecursion(2)
getSumRecursion(3)
