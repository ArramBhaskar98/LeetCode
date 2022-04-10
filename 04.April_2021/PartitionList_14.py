# 1. First converting the entire root node to one List
# 2. Passing that one list to partition into two lists based on condition
# 3. After operations combining two parition list to one list.
# 4. converting that combined list to ListNode again.

class ListNode:
	def __init__(self, val=0, next = None):
		self.val = val
		self.next = next
class Solution:
	def partition(self, head, x):
		if not head:
			return head
		result = ListNode()
		tail=result;
		self.data = []
		self.appending(head)
		self.partitionList(self.data, x)
		print('--', self.data)
		print('p3: ', self.p3)

		for x in range(len(self.p3)-1):
			tail.val = self.p3[x]
			tail.next = ListNode()
			tail = tail.next
		tail.val = self.p3[-1]
		tail.next = None
		# The below line is to check whether we converted list to ListNode successfully or not
		self.PrintList(result)

	def appending(self, head):
		self.data.append(head.val)
		if head.next:			
			self.appending(head.next)

	def partitionList(self, list, x):
		self.p1 = []
		self.p2 = []
		for item in list:
			if item < x:
				self.p1.append(item)
			else:
				self.p2.append(item)
		self.p3 = self.p1 + self.p2			
		print('p1: ', self.p1)
		print('p2: ', self.p2)

	def PrintList(self, head):
		print(head.val)
		if head.next:
			self.PrintList(head.next)

if __name__ == '__main__':

	root = ListNode(1)
	root.next = ListNode(4)
	root.next.next = ListNode(3)
	root.next.next.next = ListNode(2)
	root.next.next.next.next = ListNode(5)
	root.next.next.next.next.next = ListNode(2)

	solution = Solution()
	solution.partition(root, 3)
	