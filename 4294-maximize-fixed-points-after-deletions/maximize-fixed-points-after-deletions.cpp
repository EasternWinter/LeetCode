class Solution {
public:
    int maxFixedPoints(vector<int>& nums) {
        vector<int> s;
        vector<pair<int, int>> B;
        for (int i = 0; i < nums.size(); ++i) {
            if (i >= nums[i]) {
                B.push_back({i-nums[i], nums[i]});
            }
        }
        sort(B.begin(), B.end());
        for (auto& p : B) {
            int x = p.second;
            auto it = lower_bound(s.begin(), s.end(), x);
            if (it == s.end()) {
                s.push_back(x);
            }
            else {
                *it = x;
            }
        }
        return s.size();
    }
};