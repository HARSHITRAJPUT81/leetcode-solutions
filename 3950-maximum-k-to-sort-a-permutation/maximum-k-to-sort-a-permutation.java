
class Solution {
    public int sortPermutation(int[] nums) {
        int n = nums.length;

        // Check if the array is already sorted
        boolean sorted = true;
        for (int i = 0; i < n; i++) {
            if (nums[i] != i) {
                sorted = false;
                break;
            }
        }

        if (sorted) {
            return 0;
        }

        int ans = -1;

        // Every misplaced element must be movable.
        // A valid k must be a bitwise subset of each
        // misplaced element and its target index.
        for (int i = 0; i < n; i++) {
            if (nums[i] != i) {
                ans &= nums[i] & i;
            }
        }

        return ans;
    }
}
