from itertools import combinations
class Solution:
    def subsets(self, nums):
        lst = [[]]
        for num in nums:
            lst.append([num])
        for i in range(2,len(nums)+1):
            lst.extend(list(combinations(nums,i)))
        return lst
    
        # Creating a string. i.e [1,2,3] ==> "123"
        s = ''
        for num in nums:
            s += str(num)
        
        ans = []        # Append all the binary numbers of mask and submask subsets
        mask = 0
        for ch in s:
            mask |= 1 << (ord(ch)-ord('0'))
        
        ans.append(bin(mask)[2:])
        
        submask = mask
        while submask:
            submask = (submask-1)&mask
            ans.append(bin(submask)[2:])

        res = []
        for item in ans:
            sub = []
            for ind,val in enumerate(item[::-1]):
                if val == '1':
                    sub.append(ind)
            res.append(sub)
        return res
        