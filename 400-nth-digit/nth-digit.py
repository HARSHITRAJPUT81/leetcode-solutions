class Solution:
    def findNthDigit(self, n: int) -> int:

        digits = 1
        count = 9
        start = 1

        # Find the correct digit-length group
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # Find the actual number
        number = start + (n - 1) // digits

        # Find the required digit
        index = (n - 1) % digits

        return int(str(number)[index])