# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def constructListNode(self, lst):
        root = ListNode()
        node = root
        while lst:
            node.val = lst.pop(0)
            if lst:
                node.next = ListNode()
                node = node.next
        return root
    
    def constructList(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        print(lst)
        return lst

    def removeElements(self, head, val: int):
        # Optimal Method
        if not head:
            return None
        prev = head
        curr = head.next
        while curr:
            if curr.val != val:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        if head.val == val:
            head = head.next
        return head

        # Long-Method
        if not head:
            return None
        lst = []
        while head:
            if head.val != val:
                lst.append(head.val)
            head = head.next
            
        if not lst:
            return None
        
        root = ListNode()
        i = root
        while lst:
            i.val = lst.pop(0)
            if lst:
                i.next = ListNode()
                i = i.next
        return root

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(head = [1,2,6,3,4,5,6], val = 6, Output = [1,2,3,4,5]),
            dict(head = [6,6,1,2,3,6,3,6,7], val = 6, Output = [1,2,3,3,7]),
            dict(head = [7,7,7,7], val = 7, Output = [])]
    for test in tests:
        lst_to_listNode = sol.constructListNode(test['head'])
        node_to_list = sol.removeElements(lst_to_listNode, test['val'])
        assert sol.constructList(node_to_list) == test['Output']
        print("---------------------------------------------------")
    