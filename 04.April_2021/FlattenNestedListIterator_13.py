# The problem for this reference is here
# Link: https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3706/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.flat(nestedList)
    def flat(self, List):
        for item in List:
            if item.isInteger():
                self.data.append(item.getInteger())
            else:
                self.flat(item.getList())
        
            
    def next(self) -> int:
        return self.data.pop(0)
        
    
    def hasNext(self) -> bool:
        return len(self.data)
         

# Your NestedIterator object will be instantiated and called as such:
nestedList = [1,[4,[6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
	v.append(i.next())
print(v)
         

# Your NestedIterator object will be instantiated and called as such:
# if __name__ == '__main__':

# 	obj_1 = NestedInteger()
# 	obj_1.integer = 6

# 	obj_2 = NestedInteger()
# 	obj_2.integer = 4
# 	obj_2.lst = None

# 	obj_3 = NestedInteger()
# 	obj_3.lst.append(obj_1)

# 	obj_4 = NestedInteger()
# 	obj_4.lst.append(obj_2)
# 	obj_4.lst.append(obj_3)

# 	obj_5 = NestedInteger()
# 	obj_5.integer = 1

# 	obj_6 = NestedInteger()
# 	obj_6.lst.append(obj_5)
# 	obj_6.lst.append(obj_4)

# 	# nestedList = [1,[4,[6]]]
# 	i, v = NestedIterator(obj_6), []
# 	while i.hasNext():
# 		v.append(i.next())
# 	print(v)