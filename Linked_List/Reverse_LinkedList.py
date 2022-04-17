class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def constructNode(self, llist):
        root = ListNode()
        node = root
        while llist:
            node.val = llist.pop(0)
            if llist:
                node.next = ListNode()
                node = node.next
        return root

    def constructList(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def reverseList(self, head):

        # Recursive Approach
        def recursive(prev, curr):
            if curr:
                temp = curr.next
                curr.next = prev
                return recursive(curr, temp)
            else:
                return prev
        return recursive(None, head)

        # Iterative Approach
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(llist = [1,2,3,4,5], Output = [5,4,3,2,1]),
            dict(llist = [1,2,3], Output = [3,2,1])]
    for test in tests:
        node = sol.constructNode(test['llist'])
        ans = sol.reverseList(node)
        result = sol.constructList(ans)
        print(result)
        assert result == test['Output']
        print("-----------------------------------------")