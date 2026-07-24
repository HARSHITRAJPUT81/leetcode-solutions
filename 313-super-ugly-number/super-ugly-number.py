class Solution:
    def nthSuperUglyNumber(self, n, primes):
        m = len(primes)

        ugly = [1] * n
        idx = [0] * m

        for i in range(1, n):
            nxt = min(primes[j] * ugly[idx[j]] for j in range(m))
            ugly[i] = nxt

            for j in range(m):
                if primes[j] * ugly[idx[j]] == nxt:
                    idx[j] += 1

        return ugly[-1]