# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bst(self, node):
        lst = [node]
        ans = []
        while lst:
            n = lst.pop(0)
            ans.append(n.val)
            if n.left:
                lst.append(n.left)
            if n.right:
                lst.append(n.right)
        print(ans)
        return ans

    def deleteNode(self, root, key: int):

        # 1. Firstly find the key in BST.
        # 2. After finding the key if that key_node doesn't have left and right child, simply remove
        # that key_node i.e head = None
        # 3. If key_node has right child, then find the smallest element from that right child and 
        # replace key_node with this smallest value
        # 4. If key_node has left child, then find the largest element from that left child and 
        # replace key_node with this largest value.


        def successor(sub):
            # returning the smallest value from right child
            while sub.left:
                sub = sub.left
            return sub.val

        def predecessor(sub):
            # returning the largest value from left child
            while sub.right:
                sub = sub.right
            return sub.val        

        def recursive(head, key):
            if not head:
                return None
            if key < head.val:
                head.left = recursive(head.left, key)
            elif key > head.val:
                head.right = recursive(head.right, key)
            else:
                if not head.left and not head.right:
                    head = None
                elif head.right:
                    head.val = successor(head.right)
                    head.right = recursive(head.right, head.val)
                else:
                    head.val = predecessor(head.left)
                    head.left = recursive(head.left, head.val)
            return head

        return recursive(root, key)

if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    tests = [dict(root = root1, key = 3, Output = [5,4,6,2,7]),
            dict(root = root2, key = 0, Output = [5,3,6,2,4,7])]
    for test in tests:
        ans = sol.deleteNode(test['root'], test['key'])
        assert sol.bst(ans) == test['Output']
        print("-------------------------------------")