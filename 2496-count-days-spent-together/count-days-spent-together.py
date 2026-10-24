class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDays(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        a1 = getDays(arriveAlice)
        a2 = getDays(leaveAlice)
        b1 = getDays(arriveBob)
        b2 = getDays(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)