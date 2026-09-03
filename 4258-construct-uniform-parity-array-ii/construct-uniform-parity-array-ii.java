class Solution {
    public boolean uniformArray(int[] nums1) {
        int minOdd = Integer.MAX_VALUE;

        // Find the smallest odd number
        for (int x : nums1) {
            if (x % 2 != 0) {
                minOdd = Math.min(minOdd, x);
            }
        }

        // If there is no odd number,
        // all numbers are even, so answer is true.
        if (minOdd == Integer.MAX_VALUE) {
            return true;
        }

        // Every even number must be >= minOdd
        for (int x : nums1) {
            if (x % 2 == 0 && x < minOdd) {
                return false;
            }
        }

        return true;
    }
}
