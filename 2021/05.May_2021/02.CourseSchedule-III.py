# The Main Aim of the solution is to get Maximum number of courses done by the end of the last day.
# The Intution behind this problem is more general
# 1. We need to sort the courses list on lastday paramter in ascending order. By doing this we get 
# least duration time so that we can complete maximum number of courses.
# 2. Intially I place sumCourse = 0. for every iteration I check whether previous sumCourse done till 
# now + current duration is exceeding the lastday limit.
# 3. if limit doesn't exceeds then I push that current duration to heap and increment the sumCourse.
# 4.i If current duration exceeds the limit, then I pop the maximum course done earlier and I check again
# whether this popped element is less than current duration. If this happens I again push this popped
# element to heap and continue for next item.
# 4.ii If popped element is greater than current duration then I even decrease that maximum done course
# from Total sumCourse done till now.

import heapq
class Solution:
	def scheduleCourse(self, courses):
		sumCourse = 0
		lst = []
		courses.sort(key = lambda x: x[1])

		for duration, end in courses:
			if duration > end:
				continue
			if sumCourse + duration > end:
				a = -1 * heapq.heappop(lst)
				if a < duration:
					heapq.heappush(lst, -1 *a)
					continue
				sumCourse -= a
			heapq.heappush(lst, -1*duration)
			sumCourse += duration
		print(lst, len(lst))
		return len(lst)		

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]], Output = 3),
			dict(courses = [[1,2]], Output = 1),
			dict(courses = [[3,2],[4,3]], Output = 0),
			dict(courses = [[100, 200],[2000, 2200],[150, 300],[3000,3500]], Output = 3),
			dict(courses = [[5,5],[4,6],[2,6]], Output = 2),
			dict(courses = [[5,7],[3,5],[10,18],[4,16],[10,14]], Output = 3),
			dict(courses = [[7,11],[1,11],[1,3],[2,6],[5,6],[7,7],[4,8],[2,20],[1,17],[8,11]], Output = 6),
			dict(courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]], Output = 4)]
	for test in tests:
		assert sol.scheduleCourse(test['courses']) == test['Output']
		print('-----------------------------------------')
        