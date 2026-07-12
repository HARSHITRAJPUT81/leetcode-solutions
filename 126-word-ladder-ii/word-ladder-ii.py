from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()

            # Remove current level words so they aren't revisited
            wordSet -= level

            for word in level:
                chars = list(word)

                for i in range(len(chars)):
                    original = chars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        chars[i] = c
                        newWord = "".join(chars)

                        if newWord in wordSet:
                            parents[newWord].append(word)
                            next_level.add(newWord)

                            if newWord == endWord:
                                found = True

                    chars[i] = original

            level = next_level

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])

        return ans