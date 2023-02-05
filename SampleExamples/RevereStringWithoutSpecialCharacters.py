class Solution:
    def reverseStringWithOutSpecialCharacters(self, S):
        # Optimized Version
        # i = 0
        # j = len(S)-1
        # lst = list(S)
        # while i < j:
        #     if not S[i].isalnum():
        #         i += 1
        #     elif not S[j].isalnum():
        #         j -= 1
        #     else:
        #         lst[i], lst[j] = lst[j], lst[i]
        #         i += 1
        #         j -= 1
        # ans = "".join(lst)
        # print(ans)
        # return ans

        # My Version
        s = ""  # Taking the string without special characters
        for i in range(len(S)):
            if S[i].isalnum():
                s += S[i]
        s = s[::-1]     # reversing the string without special characters
        for i in range(len(S)):     # Iterating on Original String
            if not S[i].isalnum():  # If special character found, appending to reversed sting
                s = s[:i] + S[i] + s[i:]
        print("final s: ",s)
        return s


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(S = "intell#ect", Output = "tcelle#tni"),
             dict(S = "h@ello", Output = "o@lleh"),
             dict(S = "c#b@a", Output = "a#b@c"),
             dict(S = "abc/defgh$ij", Output = "jih/gfedc$ba"),
             dict(S = "#e @doct @eeLevoLI", Output = "#I @Love @Leetcode"),
             dict(S = "!goD @yzaLr #evOsp $muJ %xoFnw ^orBk &ciuQ *ehT", Output = "!The @Quick #Brown $Fox %Jumps ^Over &Lazy *Dog")]
    for test in tests:
        assert sol.reverseStringWithOutSpecialCharacters(test['S']) == test['Output']
        print("-----------------------------------------")