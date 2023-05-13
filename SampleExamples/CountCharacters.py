
class Solution:
    def countCharacters(self, string):
        string += '#'
        prev_char = string[0]
        result = ""
        char_count = 1
        for curr_char in string[1:]:
            if curr_char == prev_char:
                char_count += 1
            else:
                result += str(char_count) + prev_char
                char_count = 1
            prev_char = curr_char

        print("Result: ", result)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(string="aaabbbcca", result="3a3b2c1a"),
             dict(string="aaabbbccaa", result="3a3b2c2a")]
    for test in tests:
        assert sol.countCharacters(test['string']) == test['result']
        print("---------------------------------------------------")