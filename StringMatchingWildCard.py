# http:#www.geeksforgeeks.org/wildcard-character-matching/
# * --> Matches with 0 or more instances of any character or set of characters.
# ? --> Matches with any one character.
class wildCard:
  def __init__(self, txt, pat):
    self.txt = txt
    self.pat = pat

  def recursion(self, i, j):
    if i < 0 and j < 0:
      return True
    if j < 0: 
      return False
    if self.pat[j] == '?' or self.pat[j] == self.txt[i]:
      return self.recursion(i - 1, j - 1)
    if self.pat[j] == '*':
      return self.recursion(i - 1, j - 1) \
        or self.recursion(i - 1, j)
    return False

  def wildCardMatch(self):
    print self.recursion(len(self.txt) - 1, len(self.pat) - 1)

  def memorizeDP(self, i, j):
    if (i, j) not in self.cache:
      self.cache[(i, j)] = self.recursionDP(i, j)
    return self.cache[(i, j)]

  def recursionDP(self, i, j):
    self.cache = {}
    if i < 0 and j < 0:
      return True
    if j < 0: 
      return False
    if self.pat[j] == '?' or self.pat[j] == self.txt[i]:
      return self.memorizeDP(i - 1, j - 1)
    if self.pat[j] == '*':
      return self.memorizeDP(i - 1, j - 1) \
        or self.memorizeDP(i - 1, j)
    return False

  def wildCardMatchDP(self):
    print self.recursionDP(len(self.txt) - 1, len(self.pat) - 1)


wildCard("geeks", "g*ks").wildCardMatchDP(); # Yes
wildCard("geeksforgeeks", "ge?ks*").wildCardMatchDP(); # Yes
wildCard("gee", "g*k").wildCardMatchDP();  # No because 'k' is not in second
wildCard("pqrst", "*pqrs").wildCardMatchDP(); # No because 't' is not in first
wildCard("abcdhghgbcd", "abc*bcd").wildCardMatchDP(); # Yes
wildCard("abcd", "abc*c?d").wildCardMatchDP(); # No because second must have 2 instances of 'c'
wildCard("abcd", "*c*d").wildCardMatchDP(); # Yes
wildCard("abcd", "*?c*d").wildCardMatchDP(); # Yes