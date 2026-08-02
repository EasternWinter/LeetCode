class Solution {
public:
    long long getGCD(long long a, long long b) {
        return b == 0 ? a : getGCD(b, a % b);
    }
    long long maxPairStrength(vector<int>& nums) {
        long long n = nums.size();
        long long ans = 0;
        for (long long i = 0; i < n; i++) {
            for (long long j = i + 1; j < n; j++) {
                long long g = getGCD(nums[i], nums[j]);
                long long strength = ((long long)nums[i] * (long long)nums[j]) / (g * g);
                if (strength > ans) {
                    ans = strength;
                }
            }
        }
        return ans;
    }
};