# Here one thing we should keep in mind while converting Integer to Roman, Dictionary should always
# from Largest to Smallest, because Largest numbers always matches the largest Roman Numbers first,
# If those are not then it will match the smallest numbers in dictionary.

class Solution():
    def intToRoman(self, num: int) -> str:
        d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",
             9: "IX", 5: "V", 4: "IV", 1: "I"}
        res = ""
        for key, value in d.items():
            while num >= key:
                res += value
                num -= key
        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(num = 3, Output = "III"),
             dict(num = 58, Output = "LVIII"),
             dict(num = 1994, Output = "MCMXCIV")]
    for test in tests:
        assert sol.intToRoman(test['num']) == test['Output'], "Test Case Failed....!"
        print("----------------------------------------")
