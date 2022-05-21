class Solution:
    def maxConsecutive(self, bottom: int, top: int, special) -> int:
        """ The main aim of the problem is to get the maximum consecutive floors without special floors including
         in it
         1. Getting the difference between special floors gives the max difference of consecutive floors
         2. Along with that we need to handle bottom and top floors because we don't know either max consecutive
         floor may come at bottom point or middle or at the top point."""
        special.sort()
        ans = max(special[0] - bottom, top - special[-1])
        # special = [bottom-1] + special + [top+1] # also gives same answer. pls comment the above line
        # ans = 0
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(bottom=2, top=9, special=[4, 6], Output=3),
             dict(bottom=2, top=9, special=[4, 6, 8], Output=2),
             dict(bottom=6, top=8, special=[7, 6, 8], Output=0)]
    for test in tests:
        assert sol.maxConsecutive(test['bottom'], test['top'], test['special']) == test['Output']
        print("-----------------------------------------------------------")
