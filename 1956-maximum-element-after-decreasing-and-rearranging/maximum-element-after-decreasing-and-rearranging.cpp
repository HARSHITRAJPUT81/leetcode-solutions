class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {

        // Step 1: Sort the array
        sort(arr.begin(), arr.end());

        // First element must be 1
        arr[0] = 1;

        // Step 2: Make every next element
        // at most previous + 1
        for (int i = 1; i < arr.size(); i++) {
            arr[i] = min(arr[i], arr[i - 1] + 1);
        }

        // Last element will be the maximum
        return arr.back();
    }
};