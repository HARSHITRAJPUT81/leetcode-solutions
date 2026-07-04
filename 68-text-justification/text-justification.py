class Solution:
    def fullJustify(self, words, maxWidth):

        res = []
        i = 0
        n = len(words)

        while i < n:

            j = i
            length = 0

            # Take as many words as possible
            while j < n and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - length

            line = ""

            # Last line or single word
            if j == n or num_words == 1:

                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:

                gaps = num_words - 1

                even = total_spaces // gaps
                extra = total_spaces % gaps

                for k in range(i, j - 1):

                    line += words[k]

                    spaces = even
                    if extra > 0:
                        spaces += 1
                        extra -= 1

                    line += " " * spaces

                line += words[j - 1]

            res.append(line)
            i = j

        return res