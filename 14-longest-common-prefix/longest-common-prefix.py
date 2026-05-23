class Solution:
    def longestCommonPrefix(self, strs):
        
        # Take the first word as starting prefix
        prefix = strs[0]

        # Check the prefix with all words
        for word in strs[1:]:

            # Keep removing last character
            # until the word starts with prefix
            while word.startswith(prefix) == False:
                prefix = prefix[:-1]

                # If prefix becomes empty
                if prefix == "":
                    return ""

        return prefix
        