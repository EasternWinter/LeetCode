class Solution {
public:
    int countRatioSubarrays(vector<int>& nums, int a, int b) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int even = 0;
            int odd = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] % 2 == 1) {
                    odd++;
                }
                else {
                    even++;
                }
                if (odd > 0 && 1LL * even * b <= 1LL * a * odd) {
                    count++;
                }
            }
        }
        return count;
    }
};