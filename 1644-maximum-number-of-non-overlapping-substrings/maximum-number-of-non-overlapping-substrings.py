class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        # Find the smallest valid interval starting at 'start'
        def get_interval(start):
            end = last[ord(s[start]) - ord('a')]
            i = start

            while i <= end:
                c = ord(s[i]) - ord('a')

                # This character appeared before start,
                # so this interval cannot be valid.
                if first[c] < start:
                    return None

                # We must include all occurrences of this character.
                end = max(end, last[c])
                i += 1

            return (start, end)

        intervals = []

        for i in range(n):
            # Only start from the first occurrence of a character
            if i == first[ord(s[i]) - ord('a')]:
                interval = get_interval(i)

                if interval is not None:
                    intervals.append(interval)

        # Greedy: choose intervals with earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result