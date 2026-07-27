class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        n = min(n, 10)

        ans = 10          # numbers with at most 1 digit
        unique = 9        # count for current digit length
        available = 9     # remaining digits

        for _ in range(2, n + 1):
            unique *= available
            ans += unique
            available -= 1

        return ans