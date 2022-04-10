# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def levelOrder(self, root):
		if not root:
			return None
		queue = [(root, 0)]
		d = defaultdict(list)
		while queue:
			node, curr_level = queue.pop(0)
			d[curr_level].append(node.val)
			print(d)

			if node.left:
				queue.append((node.left, curr_level+1))
			if node.right:
				queue.append((node.right, curr_level+1))
			
		return list(d.values())


if __name__ == '__main__':
	root = TreeNode(3)

	root.left = TreeNode(9)
	root.right = TreeNode(20)

	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	result = Solution().levelOrder(root)
	print('Final Result: ', result)