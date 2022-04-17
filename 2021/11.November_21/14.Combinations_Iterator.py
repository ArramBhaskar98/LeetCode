from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.lst = list(combinations(characters, combinationLength))

    def next(self) -> str:
        return ''.join(self.lst.pop(0))

    def hasNext(self) -> bool:
        return self.lst


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()