from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        mid = ""

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch

        cnt = Counter({ch: freq[ch] // 2 for ch in sorted(freq)
                       if freq[ch] // 2 > 0})

        n = sum(cnt.values())

        def count_ways(counts, limit):
            total = 1
            used = 0

            for c in counts.values():
                total *= comb(used + c, c)
                if total >= limit:
                    return limit
                used += c

            return total

        if count_ways(cnt, k) < k:
            return ""

        result = []

        while n:
            for ch in sorted(cnt):
                if cnt[ch] == 0:
                    continue

                cnt[ch] -= 1
                ways = count_ways(cnt, k)

                if ways < k:
                    k -= ways
                    cnt[ch] += 1
                else:
                    result.append(ch)
                    n -= 1
                    break

        left = "".join(result)
        return left + mid + left[::-1]