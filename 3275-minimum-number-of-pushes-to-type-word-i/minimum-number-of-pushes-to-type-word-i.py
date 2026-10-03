class Solution:
    def minimumPushes(self, word):
        n = len(word)

        answer = 0

        for i in range(n):
            pushes = (i // 8) + 1
            answer += pushes

        return answer