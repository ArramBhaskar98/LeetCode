# Problem Link: https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3712/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
    	# Assigning same head address to fast and slow pointers
    	fast_ptr = head
    	slow_ptr = head

    	# Incrementing fast pointer by n steps. therefore the difference between slow_pointer and 
    	# fast pointer is n_steps.
    	for i in range(n):
    		fast_ptr = fast_ptr.next

    	# If fast_pointer next value has None, then it return's its head.next value
    	if not fast_ptr:
    		return head.next

    	while fast_ptr.next:
    		fast_ptr = fast_ptr.next
    		slow_ptr = slow_ptr.next
    	slow_ptr.next = slow_ptr.next.next
    	return head

    def PrintList(self, root):
    	print(root.val)
    	if root.next:
    		self.PrintList(root.next)
        

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

sol = Solution()
result = sol.removeNthFromEnd(root, 3)
if result:
	sol.PrintList(result)
else:
	print(result)