class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)

        left = []
        middle = ""

        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))

            if freq[ch] % 2 == 1:
                middle = ch

        left = ''.join(left)

        return left + middle + left[::-1]