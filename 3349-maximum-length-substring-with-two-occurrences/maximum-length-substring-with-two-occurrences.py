class Solution:
    def maximumLengthSubstring(self, s):
        freq = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # If any character occurs more than 2 times
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            # Current window is valid
            max_len = max(max_len, right - left + 1)

        return max_len