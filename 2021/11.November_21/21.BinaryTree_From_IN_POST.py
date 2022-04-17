# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        self.pointer = -1
        

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3], Output = [3,9,20,None,None,15,7])]

    for test in tests:
        assert sol.buildTree(test['inorder'], test['postorder']) == test['Output']
        print("----------------------------------------------------------------")
        