class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        # Reference- https://leetcode.com/problems/decode-the-slanted-ciphertext/

        txt = len(encodedText)
        cols = txt // rows
        answer = ''

        # Example: Slicing the encodedText with step as cols
        decode = [encodedText[i:i+cols] for i in range(0, txt, cols)]
        print(decode)

        for j in range(cols):
            for i in range(rows):
                if i+j < cols:
                    answer += decode[i][i+j]
        print(answer)
        return answer.rstrip()

        # Traversing through Matrix.
        matrix = [[0]*cols for _ in range(rows)]
        index = 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = encodedText[index]
                index += 1
                
        for j in range(cols):
            for i in range(rows):
                if i+j < cols:
                    answer += matrix[i][i+j]
        return answer.rstrip()

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(encodedText = "ch   ie   pr", rows = 3, Output = "cipher"),
            dict(encodedText = "iveo    eed   l te   olc", rows = 4, Output = "i love leetcode"),
            dict(encodedText = "coding", rows = 1, Output = "coding"),
            dict(encodedText = " b  ac", rows = 2, Output = " abc")]
    for test in tests:
        assert sol.decodeCiphertext(test['encodedText'], test['rows']) == test['Output']
        print("------------------------------------------------------------")