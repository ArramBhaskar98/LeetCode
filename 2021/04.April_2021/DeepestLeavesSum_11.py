
# 1. Creating TreeNode class and Tree Structure in main()
# 2. Creating one more Solution class with deepestLeavesSum() method
# 3. It calls PrintTree() with root node and level as zero
# 4. Then it recursively calls PrintTree() if it exists left node and similarily if it exists right 
# node until it encounters the leaf node by incrementing its count level.
# 5. Once leaf node encounter with it's associated count(level), this count(level) is checked in dictionary. If count(level)
# is not in dictionary it updates with that level. Similarily if tree traversal encounters such deepest level, then
# it adds that leaf node and update in dicionary.

class TreeNode:
	def __init__(self, val=0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	d = {}
	def deepestLeavesSum(self, root):
		self.PrintTree(root, count = 0)
		result_key = max(self.d.keys())
		result_value = self.d[result_key]

		# When multiple test cases present, dictionary holds previous test case results also, inorder
		# to overcome this we clear current dictionary items before we go to next test case.
		self.d.clear()
		
		return result_value

	def PrintTree(self, node, count):
		if node.left:
			self.PrintTree(node.left, count +1)
		if node.right:
			self.PrintTree(node.right, count+1)
		if not node.left and not node.right:
			if not self.d.get(count):
				self.d[count] = node.val
			else:
				self.d[count] += node.val
		
		
if __name__ == '__main__':
	
	root = TreeNode(6)

	root.left = TreeNode(7)
	root.right = TreeNode(8)

	root.left.left = TreeNode(2)
	root.left.right = TreeNode(7)

	root.right.left = TreeNode(1)
	root.right.right = TreeNode(3)

	root.left.left.left = TreeNode(9)	
	root.left.left.right = []
	root.left.right.left = TreeNode(1)
	root.left.right.right = TreeNode(4)
	
	root.right.left.left = []
	root.right.left.right = []
	root.right.right.left = []
	root.right.right.right = TreeNode(5)

	solution = Solution()
	final_res = solution.deepestLeavesSum(root)
	print('Final Result: ', final_res)