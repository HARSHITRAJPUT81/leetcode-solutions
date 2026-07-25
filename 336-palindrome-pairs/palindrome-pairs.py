class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: Prefix is palindrome
                if is_palindrome(prefix):
                    rev = suffix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        ans.append([word_map[rev], i])

                # Case 2: Suffix is palindrome
                # j != len(word) avoids duplicates for empty suffix
                if j != len(word) and is_palindrome(suffix):
                    rev = prefix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        ans.append([i, word_map[rev]])

        return ans