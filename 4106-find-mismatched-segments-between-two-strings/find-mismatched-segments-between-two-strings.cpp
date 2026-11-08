class Solution {
public:
    vector<vector<string>> findMismatchedSegments(string s1, string s2) {
        int n = s1.length();
        vector<vector<string>> result;
        int i = 0;
        while (i < n) {
            if (s1[i] != s2[i]) {
                int start = i;
                while (i < n && s1[i] != s2[i]) {
                    i++;
                }
                int length = i - start;
                string sub1 = s1.substr(start, length);
                string sub2 = s2.substr(start, length);
                result.push_back({sub1, sub2});
            }
            else {
                i++;
            }
        }
        return result;
    }
};