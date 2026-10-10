class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # suf[i] = length of the longest matching suffix
        # of word2 that can be matched starting at word1[i].
        suf = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]

            if suf[i + 1] < m and word1[i] == word2[m - 1 - suf[i + 1]]:
                suf[i] += 1

        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not used_mismatch:
                # Use this position as the one allowed mismatch
                # only if the remaining suffix can still match.
                remaining = m - j - 1

                if suf[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        return ans if j == m else []