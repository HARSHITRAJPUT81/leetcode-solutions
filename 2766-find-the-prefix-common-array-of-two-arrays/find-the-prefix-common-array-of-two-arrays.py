class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)

        seenA = set()
        seenB = set()

        C = []
        common = 0

        for i in range(n):
            # Add current elements
            seenA.add(A[i])
            seenB.add(B[i])

            # Check if A[i] is now present in both
            if A[i] in seenB:
                common += 1

            # Check if B[i] is now present in both
            if B[i] in seenA and A[i] != B[i]:
                common += 1

            C.append(common)

        return C