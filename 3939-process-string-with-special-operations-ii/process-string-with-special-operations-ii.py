class Solution:
    def processStr(self, s, k):
        n = len(s)
        length = [0] * n

        # Find length after every operation
        cur = 0

        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                cur += 1

            elif ch == '*':
                if cur > 0:
                    cur -= 1

            elif ch == '#':
                cur *= 2

            elif ch == '%':
                pass

            length[i] = cur

        # k is out of bounds
        if cur <= k:
            return '.'

        # Work backwards
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = length[i - 1] if i > 0 else 0

            if ch == '%':
                # Reversal
                k = length[i] - 1 - k

            elif ch == '#':
                # result = old + old
                # Second half maps back to first half
                if k >= prev:
                    k -= prev

            elif ch == '*':
                # One character was removed.
                # If k is still valid, its position doesn't change.
                pass

            elif 'a' <= ch <= 'z':
                # This character was appended.
                if k == prev:
                    return ch

        return '.'