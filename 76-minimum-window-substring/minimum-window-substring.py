from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        ans_len = float('inf')
        ans_l = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:

                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_l = left

                c = s[left]
                window[c] -= 1

                if c in need and window[c] < need[c]:
                    formed -= 1

                left += 1

        if ans_len == float('inf'):
            return ""

        return s[ans_l:ans_l + ans_len]