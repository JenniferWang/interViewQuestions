#!/usr/bin/py
# Head ends here
def pairs(a,k):
  #a contains array of numbers and k is the value of difference
  answer = 0
  cache = set()
  for val in a:
    if val in cache:
      continue
    cache.add(val)
    if val - k in cache:
      answer += 1
    if val + k in cache:
      answer += 1
  return answer
# Tail starts here
if __name__ == '__main__':
  a = map(int, raw_input().strip().split(" "))
  _a_size=a[0]
  _k=a[1]
  b = map(int, raw_input().strip().split(" "))
  print pairs(b,_k)