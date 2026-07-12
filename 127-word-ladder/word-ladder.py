from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, level = q.popleft()

            if word == endWord:
                return level

            chars = list(word)

            for i in range(len(chars)):
                original = chars[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    chars[i] = c
                    newWord = "".join(chars)

                    if newWord in wordSet:
                        q.append((newWord, level + 1))
                        wordSet.remove(newWord)   # Mark as visited

                chars[i] = original

        return 0