class Solution {
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;

        // dp[i] = maximum score difference
        // for the current interval starting at i
        int[] dp = new int[n];

        // Base case: one element
        for (int i = 0; i < n; i++) {
            dp[i] = nums[i];
        }

        // Length of interval
        for (int len = 2; len <= n; len++) {

            for (int i = 0; i + len <= n; i++) {

                int j = i + len - 1;

                // Take left
                int takeLeft = nums[i] - dp[i + 1];

                // Take right
                int takeRight = nums[j] - dp[i];

                dp[i] = Math.max(takeLeft, takeRight);
            }
        }

        // If score difference >= 0,
        // Player 1 can win or tie
        return dp[0] >= 0;
    }
}