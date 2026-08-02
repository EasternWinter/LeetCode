class Solution {
public:
    vector<int> countTasks(vector<int>& tasks, vector<int>& shifts) {
        int n = tasks.size();
        vector<long long> pref(n+1, 0);
        for(int i = 0; i < n; i++) {
            pref[i+1] = pref[i] + tasks[i];
        }
        long long total = pref[n];
        int pos = 0;
        long long done = 0;
        vector<int> ans;
        for (int s : shifts) {
            long long work = pref[pos] + done + s;
            if (work >= total) {
                ans.push_back(0);
                pos = 0;
                done = 0;
                continue;
            }
            pos = upper_bound(pref.begin(), pref.end(), work) - pref.begin() - 1;
            done = work - pref[pos];
            ans.push_back(n - pos);
        }
        return ans;
    }
};