# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
	def balanced(self, node):
		if node:
			A = len(node)//2
			t = TreeNode(node[A])
			t.left = self.balanced(node[:A])
			t.right = self.balanced(node[A+1:])
			return t

	def sortedListToBST(self, head):
		lst = []
		while head:
			lst.append(head.val)
			head = head.next
		print('Linked List: ', lst)
		return self.balanced(lst)

	def PrintTree(self, tree):
		queue = [(tree, 0)]
		prev_level = 0
		lst = []
		while queue:
			node, curr_level = queue.pop(0)
			if curr_level == prev_level:
				lst.append(node.val)
			else:
				lst.append(node.val)
			if node.left:
				queue.append((node.left, curr_level + 1))
			if node.right:
				queue.append((node.right, curr_level + 1))
			prev_level = curr_level
		return lst

if __name__ == '__main__':
	sol = Solution()

	lst = ListNode(-10)
	lst.next = ListNode(-3)
	lst.next.next = ListNode(0)
	lst.next.next.next = ListNode(5)
	lst.next.next.next.next = ListNode(9)

	res = sol.sortedListToBST(lst)
	tree_lst = sol.PrintTree(res)
	print('Final Level by Level Output: ', tree_lst)
