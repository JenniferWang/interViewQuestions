def modifiedNaiveMatching(text, pattern):
  """
  1. suppose all characters of pattern are different
  2. suppose len(text) >= len(pattern)
  """
  m = len(text)
  n = len(pattern)
  pos = 0
  index = 0
  while index < (m - n + 1):
    for pos in range(n):
      if text[index + pos] != pattern[pos]:
        break
      if pos == n - 1:
        print index,
      else:
        pos += 1
    index += max(1, pos)

modifiedNaiveMatching('ABCEABCDABCEABCD', "ABCD")