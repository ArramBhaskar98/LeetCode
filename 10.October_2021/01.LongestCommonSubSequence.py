from collections import defaultdict
import bisect 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        
        charPos1 = defaultdict(list)
        charPos2 = defaultdict(list)
        for i, c in enumerate(text1):
            charPos1[c].append(i)
        print(charPos1)
        
        for i, c in enumerate(text2):
            charPos2[c].append(i)
        print(charPos2)
        
        text1 += "$"
        heap = []
        for i in range(n-1, -1, -1):
            for idx in charPos2[text1[i]]:
                j = bisect.bisect_right(heap, idx)
                if j == 0:
                    heap.insert(0, idx)
                else:
                    heap[j-1] = idx
                
        return len(heap)

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(text1 = "abcde", text2 = "ace" , Output =3),
            dict(text1 = "abc", text2 = "abc", Output = 3),
            dict(text1 = "abc", text2 = "def", Output = 0)]
    for test in tests:
        assert sol.longestCommonSubsequence(test['text1'], test['text2']) == test['Output']
        print('-------------------------------------------------------')