class Solution:
    MOD = 1337

    def modPow(self, a, n):
        res = 1
        a %= self.MOD

        while n:
            if n & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
            n >>= 1

        return res

    def superPow(self, a: int, b: list[int]) -> int:
        if not b:
            return 1

        last = b.pop()

        part1 = self.modPow(self.superPow(a, b), 10)
        part2 = self.modPow(a, last)

        return (part1 * part2) % self.MOD