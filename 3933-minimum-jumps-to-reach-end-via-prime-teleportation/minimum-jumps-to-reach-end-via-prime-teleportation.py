class Solution:
    def minJumps(self, nums):
        from collections import defaultdict, deque

        n = len(nums)

        if n == 1:
            return 0

        # Find maximum value
        mx = max(nums)

        # Sieve of Eratosthenes
        is_prime = [True] * (mx + 1)

        if mx >= 0:
            is_prime[0] = False
        if mx >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= mx:
            if is_prime[p]:
                for x in range(p * p, mx + 1, p):
                    is_prime[x] = False
            p += 1

        # prime -> indices whose values are divisible by prime
        groups = defaultdict(list)

        for i, x in enumerate(nums):
            v = x
            d = 2

            while d * d <= v:
                if v % d == 0:
                    groups[d].append(i)

                    while v % d == 0:
                        v //= d

                d += 1

            if v > 1:
                groups[v].append(i)

        # BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0

        used_prime = set()

        while q:
            i = q.popleft()

            if i == n - 1:
                return dist[i]

            # Adjacent left
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = dist[i] + 1
                q.append(i - 1)

            # Adjacent right
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = dist[i] + 1
                q.append(i + 1)

            # Prime teleport
            x = nums[i]

            if is_prime[x] and x not in used_prime:
                used_prime.add(x)

                for j in groups[x]:
                    if dist[j] == -1:
                        dist[j] = dist[i] + 1
                        q.append(j)

                # No need to process this prime again
                del groups[x]

        return -1