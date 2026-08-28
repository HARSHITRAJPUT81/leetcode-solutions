class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = []

        for i in range(26):
            if freq[i] % 2 == 1:
                odd.append(i)

        if len(odd) > 1:
            return ""

        # Middle character
        middle = ""
        if len(odd) == 1:
            middle = chr(odd[0] + ord('a'))

        # Build counts for left half
        half_count = [x // 2 for x in freq]

        half_len = n // 2

        # Target's left half
        target_left = target[:half_len]

        # -------------------------------------------------
        # Try to make left half exactly equal to target_left
        # -------------------------------------------------

        count = half_count[:]
        possible = True

        for ch in target_left:
            idx = ord(ch) - ord('a')

            if count[idx] == 0:
                possible = False
                break

            count[idx] -= 1

        # If left half can exactly match target,
        # construct that palindrome and compare it directly.
        if possible:
            left = target_left

            palindrome = left + middle + left[::-1]

            if palindrome > target:
                return palindrome

        # -------------------------------------------------
        # Find the smallest left half > target_left
        # -------------------------------------------------

        # We try to make the first difference as far right
        # as possible.
        for pos in range(half_len - 1, -1, -1):

            count = half_count[:]

            # Use target characters before 'pos'
            valid = True

            for i in range(pos):
                idx = ord(target_left[i]) - ord('a')

                if count[idx] == 0:
                    valid = False
                    break

                count[idx] -= 1

            if not valid:
                continue

            # At 'pos', choose the smallest character
            # greater than target[pos].
            target_idx = ord(target_left[pos]) - ord('a')

            for c in range(target_idx + 1, 26):

                if count[c] == 0:
                    continue

                count[c] -= 1

                # Build the smallest possible suffix
                left = target_left[:pos]
                left += chr(c + ord('a'))

                for k in range(26):
                    left += chr(k + ord('a')) * count[k]

                palindrome = left + middle + left[::-1]

                return palindrome

        return ""