from collections import defaultdict
class WordFilter:
    
    def __init__(self, words):
        # Method-1
        self.W = " ".join(w + '#' + w for w in words[::-1])
        print(self.W)

        # Method-2
        # self.pref = collections.defaultdict(set)
        # self.suff = collections.defaultdict(set)
        # seen = set()
        # for i in range(len(words)-1,-1,-1):
        #     w = words[i]
        #     if w in seen:
        #         continue
        #     seen.add(w)
        #     for j in range(len(w)+1):
        #         self.pref[w[:j]].add(i)
        #         self.suff[w[j:]].add(i)

        # Method-3
        # self.d = {}
        # for word in range(len(words)):
        #     length = len(words[word])
        #     for i in range(length + 1):
        #         for j in reversed(range(length + 1)):
        #             symWord = words[word][:i] + '#' + words[word][j:]
        #             self.d[symWord] = word 
        

    def f(self, prefix: str, suffix: str) -> int:
        # Method-1
        print(self.W.count('#'))
        print(self.W.find(suffix+'#'+prefix))
        return self.W.count('#', self.W.find(suffix+'#'+prefix))-1

        # Method-2
        # a = self.pref[prefix]
        # b = self.suff[suffix]
        # x = a & b
        # return max(x) if x else -1

        # Method-3
        # ps = prefix+'#'+suffix
        # if ps in self.d:
        #     return self.d[ps]
        # return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)