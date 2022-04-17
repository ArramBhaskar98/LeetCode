from collections import Counter
class Solution:
    def findNumOfValidWords(self, words, puzzles):

        # Finding the bitmask of a word
        def bitmask(word):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch)-ord('a'))
            return mask
        word_map = Counter(bitmask(word) for word in words)
        print(word_map)

        ans = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0])-ord('a'))  # finding first letter of puzzle
            count = word_map[first]                 # Returns value if first letter of puzzle in word

            mask = bitmask(puzzle[1:])
            submask = mask

            while submask:
                count += word_map[first | submask]
                submask = (submask-1)&mask
            ans.append(count)
        return ans


        """1. word must have first letter of puzzles[i]
           2. Every letter of word must contain in puzzle"""
        # TLE My Approach 9/10 test cases passed.
        lst = []
        for puzz in puzzles:
            count = 0
            for word in words:
                flag = 0
                for letter in word:
                    if letter in puzz:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    count += 1
            lst.append(count)
        print(lst)
if __name__ == "__main__":
    sol = Solution()
    tests = [dict(words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"], Output = [1,1,3,2,4,0]),
            dict(words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"], Output = [0,1,3,2,0])]
    for test in tests:
        assert sol.findNumOfValidWords(test['words'], test['puzzles']) == test['Output']
        print("----------------------------------------------------------------------")