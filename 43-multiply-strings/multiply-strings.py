class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        ans = []

        for digit in res:
            if not (len(ans) == 0 and digit == 0):
                ans.append(str(digit))

        return "".join(ans)