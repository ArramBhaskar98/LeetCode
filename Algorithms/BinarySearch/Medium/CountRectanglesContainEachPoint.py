import bisect
from collections import defaultdict


class Solution:
    def countRectangles(self, rectangles, points):
        """ This problem requires to find each point of points has how many rectangles """
        """ 1 <= rectangles.length, points.length <= 5 * 104
            1 <= li, xj <= 109
            1 <= hi, yj <= 100"""

        def binarySearch(arr, pos):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right)//2
                print("*******")
                if arr[mid] >= pos:
                    right = mid
                else:
                    left = mid + 1
            return left

        d = defaultdict(list)
        ans = []
        # We are creating a key based on heights of the rectangle. All the lengths will be appended based on their
        # height.
        for ln, ht in rectangles:
            d[ht].append(ln)
        # Sorting the length values, so that we could apply binary search
        for key, value in d.items():
            value.sort()

        # As heights are having fewer values compared to lengths, we iterate on heights
        for ln, ht in points:
            count = 0
            for j in range(ht, 101):
                if j in d.keys():
                    count += len(d[j]) - binarySearch(d[j], ln)
                    # count += len(d[j]) - bisect.bisect_left(d[j], ln)     # This also works fine
            ans.append(count)
        print(ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(rectangles=[[1, 2], [2, 3], [2, 5]], points=[[2, 1], [1, 4]], Output=[2, 1]),
             dict(rectangles=[[1, 1], [2, 2], [3, 3]], points=[[1, 3], [1, 1]], Output=[1, 3])]
    for test in tests:
        assert sol.countRectangles(test['rectangles'], test['points']) == test['Output']
        print("------------------------------------------------------")
