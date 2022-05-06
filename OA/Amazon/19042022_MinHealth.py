class Solution:
    def minHealth(self, power, armor):
        """ The main aim of the problem is to return the minimum starting health for a player to win the game.
         The player health must be greater than 0 at all times. The player is allowed to use the armor only once
         in any round."""
        ans = 0
        armr = True
        for pow in power:
            if pow > armor and armr == True:
                ans += pow - armor
                armr = False
            else:
                ans += pow
        if armr == True:
            ans -= max(power)
        return ans + 1


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(power=[1, 2, 6, 7], armor=5, Output=12),
             dict(power=[1, 2, 3], armor=1, Output=6),
             dict(power=[1, 2, 3], armor=4, Output=4)]
    for test in tests:
        assert sol.minHealth(test['power'], test['armor']) == test['Output']
        print("----------------------------------------------------")
