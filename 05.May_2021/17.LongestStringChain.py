class Solution:
    def longestStrChain(self, words):
        result = 1
        words.sort(key = lambda x: len(x))
        print('Sorted words: ', words)
        d = {}
        for item in words:
            d[item] = 1
        print('Words in Dict: ', d)
        for item in words:
            for k in range(len(item)):
                curr_word = item[:k]+item[k+1:]
                if curr_word in d:
                    d[item] = d[curr_word] + 1
                    result = max(result, d[item])
        print('After transformation: ',d)
        return result

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(words = ["a","b","ba","bca","bda","bdca"], Output = 4),
            dict(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"], Output = 5),
            dict(words = ["a","b","ba","bca","bda","bdca","xbc","pcxbcf","xb","cxbc","pcxbc"], Output = 6)]
    for test in tests:
        assert sol.longestStrChain(test['words']) == test['Output']
        print('------------------------------------')