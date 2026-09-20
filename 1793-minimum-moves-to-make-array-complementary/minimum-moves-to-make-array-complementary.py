class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)

        # diff[x] represents change in number of moves
        # for target sum x
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            if a > b:
                a, b = b, a

            # Initially assume 2 moves for every sum.
            diff[2] += 2
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1

            # For exactly a+b, we need 0 moves instead of 1.
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        # Prefix sum gives moves required for each target sum
        moves = 0
        answer = float('inf')

        for target in range(2, 2 * limit + 1):
            moves += diff[target]
            answer = min(answer, moves)

        return answer