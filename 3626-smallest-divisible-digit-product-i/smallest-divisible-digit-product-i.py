class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num = n
            product = 1

            while num > 0:
                digit = num % 10
                product *= digit
                num //= 10

            if product % t == 0:
                return n

            n += 1