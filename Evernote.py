# First we need to identify a word. In this program, I assume a string is sep-
# erated by delimiters " ,.;:<>'[]{}()_?/'`~!@#$%^&*|-_\\\"=+1234567890\t\r\n\0"
# (Although we may have some problem with identifying words like "he's" or "can't")
# In the meantime, we count the appearance of each word and store the info in a 
# dictionary. This preprocessing cost O(n).
# In this file, I implement three methods to find the k most frequent words (sorted). 

# (1) find_bucket
  # In all cases, we can use Bucket sort to return the top k words, which is 
  # obviously O(n) as:
  # (1) frequencies are positive integers
  # (2) the highest frequency <= n
  # However, there might be some extreme cases where highest_freq - lowest_freq 
  # is huge, which means in the worst case, space complexity for Bucket sort will 
  # be O(n). Worse still, in bucket sort, we actually sort all the words, which is
  # unnecessary if k < n. 

#(2) find_quickSort
  # When n is large and k is small and doen't grow with n, we can use comparison-
  # based sort. First find the kth most frequent word, which costs O(n) by 
  # quick sort partitioning. Then sort the top k words to give the final answer.
  # The space complexity will be less then using bucket sort and time complexity 
  # will be O(n + klogk), which has a smaller coeffient than using minimum heap, 
  # but still reaches O(nlogn) when k grows with n.

import heapq
class Text:
  def __init__(self, s, delimiters = " ,.;:<>'[]{}()_?/'`~!@#$%^&*|-_\\\"=+1234567890\t\r\n\0"):
    self.s = s
    self.delimiters = delimiters
    self.dict = {}

  def findNextWord(self):
    index = 0
    start = 0
    while index < len(self.s):
      if self.s[index] not in self.delimiters:
        index += 1
        continue
      if self.s[start: index]:
        yield self.s[start : index]
      index += 1
      start = index
    
  def buildWordBag(self):
    for next_word in self.findNextWord():
      if next_word in self.dict:
        self.dict[next_word] += 1
      else:
        self.dict[next_word] = 1

  def find_minHeap(self, k):
    minHeap = [(-1, '') for x in range(k)]
    heapq.heapify(minHeap)
    for key in self.dict:
      if self.dict[key] > heapq.nsmallest(1, minHeap)[0][0]:
        heapq.heapreplace(minHeap, (self.dict[key], key))
    res = []
    for key in minHeap:
      res.insert(0, key[1])
    return res

  def find_bucket(self, k):
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

  def findKMostFrequentWords(self, k):
    if self.dict == {}:
      self.buildWordBag()
    k = min(k, len(self.dict))
    if len(self.dict) / k > 10:
      return self.find_minHeap(k)
    else:
      return self.find_bucket(k)

text = Text("\"Oh, no,\" she's saying, \"our $400 blender can\'t handle something this hard!\" ")
text = Text("you you you you word word word word end, has no need")
print text.findKMostFrequentWords(3)


