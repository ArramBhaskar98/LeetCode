# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.lst=[]
        self.preorder(root)
        while self.lst:
            root.val=self.lst.pop(0)
            root.left=None
            if self.lst and not root.right:
                root.right=TreeNode()
            root=root.right
    def preorder(self, root):
        if not root:
            return None
        if root:
            self.lst.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

if __name__ == '__main__':
	sol = Solution()

	root = TreeNode(1)

	root.left = TreeNode(2)
	root.right = TreeNode(5)

	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)


	root.right.right = TreeNode(6)

	sol.flatten(root)