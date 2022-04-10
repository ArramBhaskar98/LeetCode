# Problem Link: https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.lst = []
        self.printPreOrder(root)
        return self.lst
    
    def printPreOrder(self, root):
        self.lst.append(root.val)
        for child in root.children:
            if child:
                self.printPreOrder(child)
            else:
                self.lst.append(child.val)          
            
