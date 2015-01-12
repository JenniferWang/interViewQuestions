# Given an integer, return the longest zero sequences which is surrounded by 1 in 
# its binary form. say 10001001, return 3, 11000, return 0
def findLongestZeroSequence(integer):
  integer = abs(integer)
  lastOne = False
  maxLength = 0
  digit = 0
  while integer != 0:
    digit += 1
    if integer % 2 == 1:
      if lastOne:
        maxLength = max(maxLength, digit - lastOne - 1)
      lastOne = digit
    integer = integer / 2
  return maxLength

print findLongestZeroSequence(137) == 3
print findLongestZeroSequence(24) == 0
print findLongestZeroSequence(0) == 0


