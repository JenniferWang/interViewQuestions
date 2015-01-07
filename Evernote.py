# First we need to identify a word. In this program, I assume a string is sep-
# erated by delimiters " ,.;:<>[]{}()_?/'`~!@#$%^&*|-_\\\"=+1234567890\t\r\n\0"
# (However, here I treat words like "can't" as one word, not "can" and "t")
# In the meantime, I count the appearance of each word and store the info in a 
# dictionary. This preprocessing cost O(n) as looking up the set of delimiters
# costs O(1) on average.
#
# In this file, I implement two methods to find the k sorted most frequent words. 
#
# (1) find_K_BucketSort
  # In all cases, we can use Bucket sort to return the top k words, which is 
  # obviously O(n) as:
  # (1) frequencies are positive integers
  # (2) the highest frequency <= n
  # However, there might be some extreme cases where highest_freq - lowest_freq 
  # is huge, which means in the worst case, space complexity for Bucket sort will 
  # be O(n). Worse still, in bucket sort, we actually sort all the words, which is
  # unnecessary if k < n. 

#(2) find_K_QuickSort
  # When the number of different words is large and k is small and doesn't grow 
  # with n, we can use comparison based sort. First find the kth most frequent word, 
  # which costs O(n) by quick sort partitioning. Then sort the top k words to give 
  # the final answer. The space complexity will be less then using bucket sort and 
  # time complexity will be O(n + klogk), which has a smaller coeffient than using 
  # minimum heap, but still reaches O(nlogn) when k grows with n.


class Text:
  def __init__(self, s, delimiters = " ,.;:<>'[]{}()_?/`~!@#$%^&*|-_\\\"=+1234567890\t\r\n\0"):
    self.s = s
    self.delimiters = delimiters
    self.buildWordBag()

  def findNextWord(self):
    index = 0
    start = 0
    while index < len(self.s):
      if self.s[index] == '\'':
        if index + 1 < len(self.s) and self.s[index + 1] \
          not in self.delimiters and start < index:
          index += 1
          continue
      if self.s[index] not in self.delimiters:
        index += 1
        if index == len(self.s):
          yield self.s[start : index]
        continue
      if self.s[start: index]:
        yield self.s[start : index]
      index += 1
      start = index
    
  def buildWordBag(self):
    self.dict = {}
    for next_word in self.findNextWord():
      if next_word in self.dict:
        self.dict[next_word] += 1
      else:
        self.dict[next_word] = 1

  def partition(self, arr, left, right):
    pt1, pt2 = left - 1, left
    while pt2 <= right:
      if arr[pt2][1] >= arr[right][1]:
        pt1 += 1
        arr[pt1], arr[pt2] = arr[pt2], arr[pt1]
      pt2 += 1
    return pt1

  def quickSort(self, arr, left, right):
    pivot = self.partition(arr, left, right)
    if pivot - 1 > left:
      self.quickSort(arr, left, pivot - 1)
    if pivot + 1 < right:
      self.quickSort(arr, pivot + 1, right)

  def find_K_QuickSort(self, k):
    k = min(k, len(self.dict))
    arr = list(self.dict.items())
    left, right = 0, len(arr) - 1
    while left < right:
      pivot = self.partition(arr, left, right)
      if pivot == k:
        break
      if pivot < k:
        left = pivot + 1
      else:
        right = pivot - 1
    self.quickSort(arr, 0, k - 1)
    return [x[0] for x in arr[: k]]

  def find_K_BucketSort(self, k):
    k = min(k, len(self.dict))
    max_freq = self.dict[max(self.dict, key = self.dict.get)]
    min_freq = self.dict[min(self.dict, key = self.dict.get)]
    arr = [[] for x in range(max_freq - min_freq + 1)]
    for key, val in self.dict.iteritems():
      arr[val - min_freq].append(key)
    res = []
    count = k
    for i in range(max_freq - min_freq, -1, -1):
      if count < len(arr[i]):
        res += arr[i][: count]
        return res
      res += arr[i]
      count -= len(arr[i])
    return res


text = Text(" Renoir\'s painting Madame Clementine Valensi Stora (L\'Algerienne) (pictured) described it as \'horrible\'?")
print text.dict
# text = Text("a a b b a c c d d d e")
# print text.find_K_QuickSort(1)
# print text.find_K_QuickSort(2)
# print text.find_K_QuickSort(3)
# print text.find_K_QuickSort(4)
# print text.find_K_QuickSort(5)



