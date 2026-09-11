class Solution:
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000):
            # Must be even
            if num % 2 != 0:
                continue

            # Get its three digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Count required digits
            need = [0] * 10
            need[a] += 1
            need[b] += 1
            need[c] += 1

            # Count available digits
            available = [0] * 10
            for d in digits:
                available[d] += 1

            # Check if enough copies are available
            possible = True

            for d in range(10):
                if need[d] > available[d]:
                    possible = False
                    break

            if possible:
                count += 1

        return count