class Solution:
    def findDuplicate(self, paths):
        d = {}
        for path in paths:
            files = list(map(str, path.split(' ')))
            for file in files[1:]:
                x = file[file.index('(')+1:file.index(')')]
                if x in d:
                    d[x].append(files[0]+'/'+file[:file.index('(')])
                else:
                    d[x] = [files[0]+'/'+file[:file.index('(')]]
        final_lst = []
        for value in d.values():
            if len(value) > 1:
                final_lst.append(value)
        return sorted(final_lst)

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"], 
				Output = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
			dict(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"], 
				Output = [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]])]
	for test in tests:
		assert sol.findDuplicate(test['paths']) == sorted(test['Output'])
		print('------------------------------------------------')
