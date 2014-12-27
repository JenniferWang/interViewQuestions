# http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
def josephusFindLastNode(n, k):
  if n == 1:
    return 1
  return (josephusFindLastNode(n - 1, k) + k - 1) % n + 1

print josephusFindLastNode(5, 2)

# If this is a linked list, we can always use the previous strategy
def josephusLinkedList(head, k):
  length = 0
  pt = head
  while pt:
    pt = pt.next
    length += 1
  pos = josephusFindLastNode(length, k)
  pt = head
  for _ in range(pos - 1):
    pt = pt.next
  return pt

# Suppose this is a circular linked list
# remove the deleted node from the list
def josephusLinkedListLoop(head, k):
  if head.next == head:
    return head

  pre = curr = head
  for _ in range(k):
    pre = curr  # Attention
    curr = curr.next

  pre.next = curr.next
  del curr
  josephusLinkedListLoop(pre.next, k)


