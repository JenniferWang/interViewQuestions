class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def printList(self):
    pt = self
    count = 0
    while pt and count < 20:
      print pt.val, 
      pt = pt.next
      count += 1

class IntersectedLinkedLists():
  def has_loop(self, head):
    # There can only be one loop
    # Return one node in the loop
    if not head:
      return None
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if fast == slow:
        return fast
    return None

  def get_length(self, head):
    pt = head
    length = 0
    while pt:
      pt = pt.next
      length += 1
    return length

  # Assume two linkedlists have no loops
  # Determine whether they have intersection
  def is_intersected(self, head1, head2):
    pt1, pt2 = head1, head2
    if not head1 or not head2:
      return head1 == head2
    while pt1.next:
      pt1 = pt1.next
    while  pt2.next:
      pt2 = pt2.next
    return pt1 == pt2

  def find_intersct_without_loop(self, head1, head2):
    length_1 = self.get_length(head1)
    length_2 = self.get_length(head2)

    pt1, pt2 = head1, head2
    if length_1 > length_2:
      length_1, length_2 = length_2, length_1
      pt1, pt2 = pt2, pt1

    diff = length_2 - length_1
    for _ in range(diff):
      pt2 = pt2.next

    while pt1 :
      if pt1 == pt2:
        return pt1
      pt1 = pt1.next
      pt2 = pt2.next
    return None


  # Return the intersection point if there is one
  def has_intersection(self, head1, head2):
    """
    Only determine whether they are intersected
    """
    node_in_loop_1 = self.has_loop(head1)
    node_in_loop_2 = self.has_loop(head2)
    if not node_in_loop_1 and not node_in_loop_2:
      return self.find_intersct_without_loop(head1, head2)

    if (node_in_loop_1 and not node_in_loop_2) or (node_in_loop_2 and not node_in_loop_1):
      return None

    slow = node_in_loop_1
    fast = node_in_loop_1

    while True:
      if slow == node_in_loop_2 or slow.next == node_in_loop_2:
        return True
      slow = slow.next
      fast = fast.next.next
      if fast == slow:
        return False



# test 
head1 = ListNode(1)
node2 = ListNode(2); head1.next = node2
node3 = ListNode(3); node2.next = node3
node4 = ListNode(4); node3.next = node4
node4.next = node3
head2 = ListNode(5)
head2.next = node3

head1.printList()
print 
head2.printList()
print 

sol = IntersectedLinkedLists()
result = sol.has_intersection(head1, head2)

print result

      

