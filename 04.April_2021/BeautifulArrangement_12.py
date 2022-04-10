
# def constructArray(n, k):
#     seen = [False] * n
#     def num_uniq_diffs(arr):
#         ans = 0
#         for i in range(n):
#             seen[i] = False
#         for i in range(len(arr) - 1):
#             delta = abs(arr[i] - arr[i+1])
#             if not seen[delta]:
#                 ans += 1
#                 seen[delta] = True
#         return ans

#     for cand in itertools.permutations(range(1, n+1)):
#         if num_uniq_diffs(cand) == k:
#             return cand

def arrangement(n, k):
	k_lst = [x for x in range(k, 0, -1)]
	n_lst = [1]
	for item in range(n-1):
		if item >= k:
			n_lst.append(item+2)
		elif item % 2 ==0:
			n_lst.append(n_lst[item] + k_lst[item])
		else:
			n_lst.append(n_lst[item] - k_lst[item])
	return n_lst

if __name__ == '__main__':
	
	result = arrangement(92,80)
	print('Final Result: ', result)