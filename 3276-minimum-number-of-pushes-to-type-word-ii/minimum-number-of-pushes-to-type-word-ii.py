class Solution:
    def minimumPushes(self, word):
        freq = [0] * 26

        # Count frequency of every letter
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Most frequent letters should come first
        freq.sort(reverse=True)

        ans = 0

        for i in range(26):
            if freq[i] == 0:
                break

            # Every 8 letters, the push count increases
            pushes = (i // 8) + 1

            ans += freq[i] * pushes

        return ans