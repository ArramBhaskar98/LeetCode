import bisect
class Solution:
    def suggestedProducts(self, products, searchWord):
        # Method -1
        searched_suggs= []
        products.sort()
        for i in range(1, len(searchWord)+1):
            searched_words = []
            for word in products:
                if searchWord[:i] == word[:i]:
                    searched_words.append(word)
            searched_suggs.append(searched_words[:3])
        return searched_suggs

        # Method-2
        # ans = []
        # curr_word = ''
        # products.sort()
        # for letter in searchWord:
        #     curr_word += letter
        #     idx = bisect.bisect_left(products, curr_word)
        #     ans.append([product for product in products[idx:idx+3] if product.startswith(curr_word)])

        # return ans

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse",
                Output = [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"]]),
            dict(products = ["havana"], searchWord = "havana", 
                Output = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
            dict(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags", 
                Output = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]),
            dict(products = ["havana"], searchWord = "tatiana", Output = [[],[],[],[],[],[],[]])]
    for test in tests:
        assert sol.suggestedProducts(test['products'], test['searchWord']) == test['Output']
        print('---------------------------------------------------------------')