class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for x in stones:
            count[x % 3] += 1

        def check(cnt):
            # Alice starts by taking a remainder-1 stone
            if cnt[1] == 0:
                return False

            cnt[1] -= 1

            # Number of moves using alternating 1 and 2 stones
            moves = 1 + min(cnt[1], cnt[2]) * 2 + cnt[0]

            # If extra remainder-1 stone exists
            if cnt[1] > cnt[2]:
                cnt[1] -= 1
                moves += 1

            return moves % 2 == 1 and cnt[1] != cnt[2]

        # Alice can start with remainder 1
        if check(count[:]):
            return True

        # Alice can start with remainder 2
        swapped = [count[0], count[2], count[1]]

        return check(swapped)