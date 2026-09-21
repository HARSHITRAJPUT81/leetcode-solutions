class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        # Trie node:
        # [children, best_index]
        trie = [{"children": {}, "best": 0}]

        # Insert container words in reverse
        for i, word in enumerate(wordsContainer):
            node = 0

            # Update best index at root
            if self.better(i, trie[node]["best"], wordsContainer):
                trie[node]["best"] = i

            for ch in reversed(word):
                if ch not in trie[node]["children"]:
                    trie[node]["children"][ch] = len(trie)
                    trie.append({"children": {}, "best": i})

                node = trie[node]["children"][ch]

                # Update best index at this node
                if self.better(i, trie[node]["best"], wordsContainer):
                    trie[node]["best"] = i

        ans = []

        # Process queries
        for word in wordsQuery:
            node = 0

            # Default answer: best word overall
            best = trie[0]["best"]

            for ch in reversed(word):
                if ch not in trie[node]["children"]:
                    break

                node = trie[node]["children"][ch]
                best = trie[node]["best"]

            ans.append(best)

        return ans

    def better(self, i, j, wordsContainer):
        # Return True if i is better than j
        if len(wordsContainer[i]) < len(wordsContainer[j]):
            return True

        if len(wordsContainer[i]) == len(wordsContainer[j]) and i < j:
            return True

        return False