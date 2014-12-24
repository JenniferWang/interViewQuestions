class KMP:
  def __init__(self, text):
    self.text = text

  def kmp_table(self, word):
    self.table = [-1, 0]
    pos = 2 
    cnd = 0
    while pos < len(word):
      if word[pos - 1] == word[cnd]:
        cnd += 1
        self.table.append(cnd)
        pos += 1
      elif cnd > 0:
        cnd = self.table[cnd]
      else:
        self.table.append(0)
        pos += 1

  # implement the KMP algorithm
  def kmp_search(self, word):
    self.kmp_table(word)
    m = 0 # the beginning of the current match in S
    i = 0 # the position of the current character in word
    occur = []
    while m + i < len(self.text):
      if self.text[m + i] == word[i]:
        if i == len(word) - 1:
          occur.append(m)
          m += i + 1
          i = 0
          continue
        else:
          i += 1
      else:
        if self.table[i] > -1:
          m += i - self.table[i]
          i = self.table[i]
        else:
          i = 0
          m += 1
    print occur


test = KMP('ABCDABD ABCDABD')
test.kmp_search('ABCDABD')
