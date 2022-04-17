# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def contructLink(self, lst):
        lnode = node = ListNode()
        while lst:
            node.val = lst.pop(0)
            if lst:
                node.next = ListNode()
                node = node.next
        if lnode.val == 0:
            return lnode.next
        return lnode
    
    def constructList(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        print(lst)
        return lst

    def oddEvenList(self, head):
        if not head:
            return None
        p = prev = head
        c = curr = head.next
        while prev or curr:
            if prev.next and prev.next.next:
                prev.next = prev.next.next
                prev = prev.next
            else:
                prev.next = c
                break
            if curr.next and curr.next.next:
                curr.next = curr.next.next
                curr = curr.next
            else:
                curr.next = None
        return p


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(head = [1,2,3,4,5], Output = [1,3,5,2,4]),
            dict(head = [2,1,3,5,6,4,7], Output = [2,3,6,7,1,5,4]),
            dict(head = [1,2,3,4,5,6], Output = [1,3,5,2,4,6]),
            dict(head = [], Output = [])]
    for test in tests:
        node = sol.contructLink(test['head'])
        ans = sol.oddEvenList(node)
        assert sol.constructList(ans) == test['Output']
        print("----------------------------------------")
    