# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:

        def recursive(root, k):
            if root.val in d:
                return True
            else:
                d[k-root.val] = root.val
                if root.left and recursive(root.left, k):
                    return True
                if root.right and recursive(root.right, k):
                    return True
        d = {}
        return True if recursive(root, k) else False


if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(5)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(2)
    t1.left.right = TreeNode(4)
    t1.right = TreeNode(6)
    t1.right = TreeNode(7)

    tests = [dict(root = t1, k = 9, Output = True),
             dict(root = t1, k = 28, Output = False)]
    for test in tests:
        ans = sol.findTarget(test['root'], test['k'])
        print("Answer: ", ans)
        assert ans == test['Output']
        print("-----------------------------------------------")