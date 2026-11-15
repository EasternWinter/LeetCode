class Solution {
public:
    int countConsistent(vector<int>& nums) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; ++i) {
            int curAnd = nums[i];
            int curMin = nums[i];
            for (int j = i; j < n; ++j) {
                curAnd &= nums[j];
                curMin = min(curMin, nums[j]);
                if (curAnd == curMin) {
                    ++count;
                }
            }
        }
        return count;
    }
};