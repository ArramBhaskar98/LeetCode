class Solution:

    def fullBloomFlowers(self, flowers, persons):
        """You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith
        flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

        Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom
        when the ith person arrives."""

        # method-1
        # A, B = sorted(a for a,b in flowers), sorted(b for a,b in flowers)
        # return [bisect_right(A, p)-bisect_left(B, p) for p in persons]

        # Method - 2
        def binarySearch_right(arr, pos):
            """ This function is similar to bisect.bisect_right() """
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > pos:
                    right = mid
                else:
                    left = mid + 1
            return left

        def binarySearch_left(arr, pos):
            """ This function is similar to bisect.bisect_left """
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= pos:
                    right = mid
                else:
                    left = mid + 1
            return left

        A, B = sorted(a for a, b in flowers), sorted(b for a, b in flowers)
        return [binarySearch_right(A, p) - binarySearch_left(B, p) for p in persons]

        # Method - 3
        # Brute-Force - TLE
        # d = {}
        # ans = []
        # for st,et in flowers:
        #     for num in range(st, et+1):
        #         if num not in d:
        #             d[num] = 1
        #         else:
        #             d[num] += 1
        # for per in persons:
        #     if per in d.keys():
        #         ans.append(d[per])
        #     else:
        #         ans.append(0)
        # return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], persons=[2, 3, 7, 11], Output=[1, 2, 2, 2]),
             dict(flowers=[[1, 10], [3, 3]], persons=[3, 3, 2], Output=[2, 2, 1])]
    for test in tests:
        assert sol.fullBloomFlowers(test['flowers'], test['persons']) == test['Output']
        print("----------------------------------------------")
