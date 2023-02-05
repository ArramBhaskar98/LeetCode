class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """" Replacing only single character with any lowercase english letter so that resulting string is not a
        palindromic and that is lexicographically smallest one. """
        
        n = len(palindrome)
        if n == 1:
            return ""
        for index in range(n//2):
            if palindrome[index] != 'a':
                return palindrome[:index] + 'a' + palindrome[index+1:]
        return palindrome[:n-1] + 'b'


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(palindrome = "abccba", Output = "aaccba"),
             dict(palindrome = "a", Output = ""),
             dict(palindrome = "bbbzzbbb", Output = "abbzzbbb"),
             dict(palindrome = "aaaaaa", Output = "aaaaab")]
    for test in tests:
        assert sol.breakPalindrome(test['palindrome']) == test['Output'], "Test Case Failed...!"
        print("-----------------------------------------------")