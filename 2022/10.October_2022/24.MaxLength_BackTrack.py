from typing import List
# Problem - https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

""" This Problem can be solved using two methods one is DP and BackTracking
    1.  Using BackTracking
        The main aim of the problem is, A string s is formed by the concatenation of a subsequence of arr that
        has unique characters. BackTrack always check the success condition and Failure condition.
        * Let's create a empty set and start creating a string. 
        * Success Condition : After adding previous set elements with current string elements equals with unique
        elements of temp set, then further recursion check will happen with temp set.
        * Even after Success condition, it will check all the possibilities with failure condition too. """

class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # Method -2 DP
        dp = [set()]
        for s in arr:
            if len(set(s)) < len(s):
                continue
            s = set(s)
            for d in dp:
                if s & d:
                    continue
                dp.append(s | d)
        return max(len(x) for x in dp)

        # My Method
        def recursive(i, s):
            if i == len(arr):       # Base Condition, If i reaches the last index, return the length of set
                return len(s)

            prev_set_size = len(s)              # Checking the previous set size
            curr_string_size = len(arr[i])      # Checking current string size.
            res1 = res2 = float('-inf')

            temp = s | set(arr[i])              # Creating a new set. s union set of current position elements

            # Validation step : temp set always contains the unique elements. Sometimes curr_string_size may
            # contain duplicate characters and hence adding with prev_set_size may be larger than union of
            # pevious_set and current set elements Eg: ["aa","bb"] test case
            if prev_set_size + curr_string_size == len(temp):
                res1 = recursive(i+1, temp)
            res2 = recursive(i+1, s)

            return max(res1, res2)

        return recursive(0, set())


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(arr = ["un","iq","ue"], Output = 4),
             dict(arr = ["cha","r","act","ers"], Output = 6),
             dict(arr = ["abcdefghijklmnopqrstuvwxyz"], Output = 26),
             dict(arr = ["aa", "bb"], Output = 0),
             dict(arr = ["a","abc","d","de","def"], Output = 6),
             dict(arr = ["a","bc","def"], Output = 6)]
    for test in tests:
        assert sol.maxLength(test['arr']) == test['Output'], "TestCase Failed...!"
        print("---------------------------------------------------")