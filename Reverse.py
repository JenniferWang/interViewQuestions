def reverseString(s):
  n = len(s):
  for i in range(n):
    s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
  return 