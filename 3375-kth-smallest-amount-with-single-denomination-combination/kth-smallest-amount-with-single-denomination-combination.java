class Solution {

    public long findKthSmallest(int[] coins, int k) {

        // Remove redundant denominations
        Arrays.sort(coins);

        List<Long> validCoins = new ArrayList<>();

        for (int coin : coins) {
            boolean redundant = false;

            for (long prev : validCoins) {
                if (coin % prev == 0) {
                    redundant = true;
                    break;
                }
            }

            if (!redundant) {
                validCoins.add((long) coin);
            }
        }

        int n = validCoins.size();

        long[] arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = validCoins.get(i);
        }

        // Binary search
        long low = 1;
        long high = (long) arr[0] * k;

        while (low < high) {

            long mid = low + (high - low) / 2;

            if (count(mid, arr) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    // Count numbers <= x divisible by at least one coin
    private long count(long x, long[] coins) {

        int n = coins.length;
        long result = 0;

        // Iterate through all non-empty subsets
        for (int mask = 1; mask < (1 << n); mask++) {

            long lcm = 1;
            int bits = 0;
            boolean valid = true;

            for (int i = 0; i < n; i++) {

                if ((mask & (1 << i)) != 0) {

                    bits++;

                    lcm = getLCM(lcm, coins[i], x);

                    // LCM > x means it contributes nothing
                    if (lcm > x) {
                        valid = false;
                        break;
                    }
                }
            }

            if (!valid) {
                continue;
            }

            long multiples = x / lcm;

            // Inclusion-Exclusion
            if (bits % 2 == 1) {
                result += multiples;
            } else {
                result -= multiples;
            }
        }

        return result;
    }

    private long getLCM(long a, long b, long limit) {

        long gcd = gcd(a, b);

        // Prevent overflow
        long value = a / gcd;

        if (value > limit / b) {
            return limit + 1;
        }

        return value * b;
    }

    private long gcd(long a, long b) {

        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }
}