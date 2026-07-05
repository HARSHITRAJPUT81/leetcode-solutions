class Solution:
    def subsets(self, nums):
        ans = []
        path = []

        def dfs(index):
            if index == len(nums):
                ans.append(path[:])
                return

            # Exclude nums[index]
            dfs(index + 1)

            # Include nums[index]
            path.append(nums[index])
            dfs(index + 1)

            path.pop()

        dfs(0)
        return ans