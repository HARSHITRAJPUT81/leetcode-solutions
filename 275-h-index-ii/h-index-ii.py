class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            papers = n - mid
            
            if citations[mid] == papers:
                return papers
            
            elif citations[mid] < papers:
                # Need higher citation count
                left = mid + 1
            
            else:
                # Try to find smaller index
                right = mid - 1
        
        # left is the first position where citations[left] >= n-left
        return n - left