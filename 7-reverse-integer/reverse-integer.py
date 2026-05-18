class Solution:
    def reverse(self, x: int) -> int:

        sign = 1

        if x < 0:
            sign = -1

        x = abs(x)

        reverse_num = 0

        while x > 0:

            digit = x % 10

            reverse_num = reverse_num * 10 + digit

            x = x // 10

        reverse_num = reverse_num * sign

        if reverse_num < -2147483648 or reverse_num > 2147483647:
            return 0

        return reverse_num