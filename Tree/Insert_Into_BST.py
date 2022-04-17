# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, bst):
        lst = [bst]
        ans = []
        while lst:
            node = lst.pop(0)
            ans.append(node.val)
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        print(ans)
        return ans

    def insertIntoBST(self, root, val: int):

        def dfs(head):
            if not head:
                return TreeNode(val)
            if head.val < val:
                head.right = dfs(head.right)
            else:
                head.left = dfs(head.left)
            return head

        return dfs(root)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    n = sol.insertIntoBST(root, 5)

    if sol.bfs(n) == [4,2,7,1,3,5]:
        print("------------------------------------------------")
    else:
        print("Wrong Answer")

