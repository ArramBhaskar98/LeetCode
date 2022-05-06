class Solution:
    def minimumCardPickup(self, cards):
        """ The main aim of the problem is to pick the minimum number of consecutive cards to have a pair of matching cards. For reference of this problem, click here"""
        ans = float('inf')
        d = {}
        for index, num in enumerate(cards):
            if num in d:
                ans = min(ans, index-d[num])
            else:
                d[num] = index
        return ans+1 if ans < float('inf') else -1


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(cards = [3,4,2,3,4,7], Output = 4),
             dict(cards = [1,0,5,3], Output = -1),
             dict(cards = [77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43], Output = 3)]
    for test in tests:
        assert sol.minimumCardPickup(test['cards']) == test['Output'], "Output is Mis-Matching."
        print("--------------------------------------------------------")