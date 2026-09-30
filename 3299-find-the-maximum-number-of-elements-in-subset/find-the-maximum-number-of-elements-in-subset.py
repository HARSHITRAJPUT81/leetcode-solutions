class Solution:
    def maximumLength(self, nums):
        from collections import Counter

        freq = Counter(nums)
        ans = 1

        for x in freq:

            # Special case: 1² = 1
            if x == 1:
                length = freq[1]

                # Length must be odd
                if length % 2 == 0:
                    length -= 1

                ans = max(ans, length)
                continue

            cur = x
            length = 0

            while True:
                nxt = cur * cur

                # To put cur on both sides,
                # we need 2 copies of cur AND cur² must exist
                if freq[cur] >= 2 and nxt in freq:
                    length += 2
                    cur = nxt
                else:
                    break

            # cur can be the middle element
            if length > 0:
                length += 1
            else:
                length = 1

            ans = max(ans, length)

        return ans