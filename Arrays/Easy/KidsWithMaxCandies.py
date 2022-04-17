class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxC = max(candies)
        lst = []
        for candy in candies:
            lst.append(candy+extraCandies>=maxC)
        return lst

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(candies = [2,3,5,1,3], extraCandies = 3, Output = [True,True,True,False,True]),
            dict(candies = [4,2,1,1,2], extraCandies = 1, Output = [True,False,False,False,False]),
            dict(candies = [12,1,12], extraCandies = 10, Output= [True,False,True])]
    for test in tests:
        assert sol.kidsWithCandies(test['candies'], test['extraCandies']) == test['Output']
        print("--------------------------------------------------------------------------")