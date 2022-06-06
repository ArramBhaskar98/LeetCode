class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # Some Optimization
        ans = ""
        for word in sentence.split():
            if '$' in word:
                try:
                    val = float(word[1:])
                    ans += "$" + "{:.2f}".format(val-(val*(discount/100))) + " "
                except:
                    ans += word+" "
            else:
                ans += word + " "
        print(ans)
        return ans.rstrip()

        # My Method
        ans = ""
        for word in sentence.split():
            if word[0] == '$' and len(word) > 1 and word[1:].isdigit():
                temp = int(word[1:])
                dis = temp - (temp*(discount/100))
                word = "$" + str(format(dis,'.2f'))
            ans += word + " "
        return ans.rstrip()


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50, Output = "there are $0.50 $1.00 and 5$ candies in the shop"),
             dict(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100, Output = "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"),
             dict(sentence = "$2$3 $10 $100 $1 200 $33 33$ $$ $99 $99999 $9999999999", discount = 0, Output = "$2$3 $10.00 $100.00 $1.00 200 $33.00 33$ $$ $99.00 $99999.00 $9999999999.00")]
    for test in tests:
        assert sol.discountPrices(test['sentence'], test['discount']) == test['Output']
        print("---------------------------------------------------------------------")