class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Not using In-Built methods
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = ''

        for i in range(max_len-1, -1, -1):
            r = carry
            if a[i] == '1':
                r += 1
            if b[i] == '1':
                r += 1
            result = ('1' if r%2 == 1 else '0') + result
            
            if r < 2:
                carry = 0
            else:
                carry = 1
        if carry != 0:
            result = '1'+ result
        print(result)
        return result

        # By using In-Built methods
        return bin(int(a,2)+int(b,2))[2:]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(a = "11", b = "1", Output = "100"),
            dict(a = "1010", b = "1011", Output = "10101"),
            dict(a = "110110101001110111101", b = "10101010110101", Output = "110110111111001110010")]
    for test in tests:
        assert sol.addBinary(test['a'], test['b']) == test['Output']
        print("---------------------------------------------------")