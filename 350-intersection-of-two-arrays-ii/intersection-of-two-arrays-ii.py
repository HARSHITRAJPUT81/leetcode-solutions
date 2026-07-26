from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums1)
        ans = []

        for num in nums2:
            if freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans