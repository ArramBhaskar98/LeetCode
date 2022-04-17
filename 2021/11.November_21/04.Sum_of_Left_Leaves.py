class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        sumLeaves = 0

        def recursive(root):
            nonlocal sumLeaves
            if not root.left and not root.right:
                sumLeaves += root.val
                return
            if root.left:
                recursive(root.left)
            if root.right and (root.right.left or root.right.right):
                recursive(root.right)

        recursive(root)
        return sumLeaves
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Another Tree
    root1 = TreeNode(4)

    root1.left = TreeNode(3)
    root1.right = TreeNode(7)

    root1.left.right = TreeNode(6)
    root1.right.right = TreeNode(4)

    root1.left.right.right = TreeNode(9)
    root1.right.right.left = TreeNode(2)
    root1.right.right.right = TreeNode(8)

    root1.left.right.right.left = TreeNode(2)
    root1.right.right.right.left = TreeNode(1)

    lst = [(root,24), (root1,5)]
    for x,y in lst:
        if sol.sumOfLeftLeaves(x) == y:
            print("====================================", y)
        else:
            print("Wrong Answer....!")