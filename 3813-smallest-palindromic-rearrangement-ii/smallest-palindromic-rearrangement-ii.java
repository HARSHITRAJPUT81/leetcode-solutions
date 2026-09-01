class Solution {

    public String smallestPalindrome(String s, int k) {
        int[] freq = new int[26];

        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        // Number of characters in the first half
        int halfLen = s.length() / 2;

        int[] half = new int[26];

        for (int i = 0; i < 26; i++) {
            half[i] = freq[i] / 2;
        }

        // If total number of distinct palindromes < k,
        // we will detect it while constructing the answer.
        StringBuilder left = new StringBuilder();

        long K = k;

        for (int pos = 0; pos < halfLen; pos++) {

            // Try characters from 'a' to 'z'
            for (int ch = 0; ch < 26; ch++) {

                if (half[ch] == 0) {
                    continue;
                }

                // Temporarily use this character
                half[ch]--;

                // Number of different permutations possible
                // with the remaining characters
                long ways = countWays(half, K);

                if (ways >= K) {
                    // This character is part of the k-th answer
                    left.append((char) ('a' + ch));
                    break;
                } else {
                    // Skip all these permutations
                    K -= ways;

                    // Put character back
                    half[ch]++;
                }
            }

            // If no character could be selected
            if (left.length() != pos + 1) {
                return "";
            }
        }

        // Build the middle character
        StringBuilder right = new StringBuilder(left).reverse();

        String middle = "";

        if (s.length() % 2 == 1) {
            for (int i = 0; i < 26; i++) {
                if (freq[i] % 2 == 1) {
                    middle = String.valueOf((char) ('a' + i));
                    break;
                }
            }
        }

        return left.toString() + middle + right.toString();
    }

    private long countWays(int[] cnt, long limit) {

        int total = 0;

        for (int x : cnt) {
            total += x;
        }

        long result = 1;

        /*
         * Calculate:
         *
         * total! / (cnt[0]! cnt[1]! ...)
         *
         * using:
         *
         * C(total, cnt[i])
         */
        for (int x : cnt) {

            if (x == 0) {
                continue;
            }

            long combinations = combination(total, x, limit);

            result = result * combinations;

            if (result >= limit) {
                return limit;
            }

            total -= x;
        }

        return result;
    }

    private long combination(int n, int r, long limit) {

        r = Math.min(r, n - r);

        long result = 1;

        for (int i = 1; i <= r; i++) {

            result = result * (n - r + i) / i;

            if (result >= limit) {
                return limit;
            }
        }

        return result;
    }
}