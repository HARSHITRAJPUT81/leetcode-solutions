class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            # First number cannot have leading zeros
            if num[0] == '0' and i > 1:
                break
            a = int(num[:i])

            for j in range(i + 1, n):
                # Second number cannot have leading zeros
                if num[i] == '0' and j - i > 1:
                    break
                b = int(num[i:j])

                x, y = a, b
                k = j

                while k < n:
                    s = str(x + y)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    x, y = y, x + y

                if k == n:
                    return True

        return False
        