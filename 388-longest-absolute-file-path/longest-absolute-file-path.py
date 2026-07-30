class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth_len = {0: 0}
        ans = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            if '.' in name:  # File
                ans = max(ans, depth_len[depth] + len(name))
            else:  # Directory
                depth_len[depth + 1] = depth_len[depth] + len(name) + 1

        return ans