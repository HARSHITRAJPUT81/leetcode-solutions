class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefix_num = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)
            prefix_num[i + 1] = prefix_num[i]
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_count[i + 1] = prefix_count[i]

            if digit != 0:
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
                prefix_sum[i + 1] += digit
                prefix_count[i + 1] += 1

        answer = []

        for l, r in queries:
            count = prefix_count[r + 1] - prefix_count[l]

            if count == 0:
                answer.append(0)
                continue

            x = (
                prefix_num[r + 1]
                - prefix_num[l] * pow(10, count, MOD)
            ) % MOD

            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            answer.append((x * digit_sum) % MOD)

        return answer