# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def node(self, llist):
        root = ListNode()
        l_node = root

        while llist:
            l_node.val = llist.pop(0)
            if llist:
                l_node.next = ListNode()
                l_node = l_node.next
        return root

    def reverseKGroup(self, head, k: int):
        if k == 1 or not head.next:
            return head
        dummy = ListNode(0, head)
        start = dummy
        end = head
        count = 0

        def reverse(s, e):
            prev, curr = s, s.next
            first = curr
            while curr != e:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            s.next = prev
            first.next = curr
            return first

        while end:
            count += 1
            if count % k == 0:
                print("Sending values: ", start.val, end.next.val)
                start = reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next

    def to_List(self, node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        print("To List: ", ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(head = [1,2,3,4,5], k = 2, Output = [2,1,4,3,5]),
            dict(head = [1,2,3,4,5], k = 3, Output = [3,2,1,4,5]),
            dict(head = [1,2,3,4,5], k = 1, Output = [1,2,3,4,5])]
    for test in tests:
        list_node = sol.node(test['head'])
        solution = sol.reverseKGroup(list_node, test['k'])
        assert sol.to_List(solution) == test['Output']
        print("---------------------------------------------------------")