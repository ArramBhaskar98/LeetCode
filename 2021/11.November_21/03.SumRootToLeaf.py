# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        lst = []

        def recursive(root, s):
            nonlocal lst
            s += root.val

            if not root.left and not root.right:
                lst.append(s)
                return
            if root.left:
                recursive(root.left, s*10)
            if root.right:
                recursive(root.right, s*10)
            
        recursive(root,0)
        return sum(lst)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)

    root.left = TreeNode(9)
    root.right = TreeNode(0)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    ans = sol.sumNumbers(root)
    if ans == 1026:
        print("------------------------------------",ans)
    else:
        print("Wrong Answer.....!")