class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a)-1, len(b)-1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:

            s = carry

            if i >= 0:
                s += ord(a[i]) - ord('0')
                i -= 1

            if j >= 0:
                s += ord(b[j]) - ord('0')
                j -= 1

            res.append(str(s % 2))
            carry = s // 2

        return ''.join(reversed(res))