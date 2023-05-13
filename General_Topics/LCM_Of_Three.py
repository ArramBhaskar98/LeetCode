
# In-order to find LCM or HCD of any numbers, we know that formulae is
# LCM(numbers) * HCF(number) = product(numbers)
# Eg: LCM(a,b) * HCF(a,b) = a * b

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    def lcm_of_three(self, lst):
        """ Initially Finding lcm of two, then finding the lcm of two with another number  """
        a, b, c = lst
        lcm_ab = (a * b) // self.gcd(a,b)
        lcm_ab_c = (lcm_ab * c) // self.gcd(lcm_ab, c)

        return lcm_ab_c


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(lst=[6,10,15], Output=30),
             dict(lst=[15,6,10], Output=30)]
    for test in tests:
        assert sol.lcm_of_three(test['lst']) == test['Output']
        print("----------------------------------------------")