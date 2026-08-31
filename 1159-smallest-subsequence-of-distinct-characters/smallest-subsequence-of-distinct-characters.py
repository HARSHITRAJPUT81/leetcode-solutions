class Solution:
    def smallestSubsequence(self, s):
        # Last occurrence of every character
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        used = set()

        for i in range(len(s)):
            ch = s[i]

            # Character already present in result
            if ch in used:
                continue

            # Remove bigger characters if they appear again later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                used.remove(removed)

            stack.append(ch)
            used.add(ch)

        return ''.join(stack)