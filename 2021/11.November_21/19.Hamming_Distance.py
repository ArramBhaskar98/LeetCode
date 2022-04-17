class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        value = x^y     # Sets to 1 only, if bits are different 
        while value > 0:
            # Peter Wegner Algorithm counts the bit 1 in a string or value
            value = value & (value-1)   # This lines clears lowest order non zero bits i.e 1 to 0
            distance += 1
        return distance

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(x = 1, y = 4, Output = 2),
            dict(x = 3, y = 1, Output = 1)]
    for test in tests:
        assert sol.hammingDistance(test['x'],test['y']) == test['Output']
        print("-----------------------------------------------------")