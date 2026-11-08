class Solution {
public:
    int countSuffix(vector<int>& nums, vector<int>& target) {
        int n = nums.size();
        unordered_map<int, int> freq;
        for (int x : nums) {
            freq[x]++;
        }
        for (int x : target) {
            if (--freq[x] < 0) {
                return 0;
            }
        }
        int first_mismatch = n - 1;
        for (int i = 0; i < n; i++) {
            if (nums[i] != target[i]) {
                first_mismatch = i;
                break;
            }
        }
        int min_sorted_idx = n - 1;
        while (min_sorted_idx > 0 && target[min_sorted_idx - 1] >= target[min_sorted_idx]) {
            min_sorted_idx--;
        }
        if (first_mismatch < min_sorted_idx) {
            return 0;
        }
        return first_mismatch - min_sorted_idx + 1;
    }
};