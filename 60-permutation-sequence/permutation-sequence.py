class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1          # convert to 0-based indexing

        ans = []

        while nums:

            index = k // fact
            ans.append(nums.pop(index))

            if not nums:
                break

            k %= fact
            fact //= len(nums)

        return "".join(ans)