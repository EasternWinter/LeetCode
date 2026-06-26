class Solution {
public:
    bool isNumber(string s) {
        /*int n = s.length();
        if (n == 1) {
            if (s[0] >= '0' && s[0] <= '9') {
                return true;
            }
            return false;
        }
        if (s[0] != '.' && (s[0] < '0' || s[0] > '9') && s[0] != '-' && s[0] != '+') {
            return false;
        }
        int ind = 1;
        set<char> visited = {};
        bool e = false;
        if (s[0] == '.') {
            visited.insert(s[0]);
        }
        while (ind < n) {
            if (s[ind] == 'e' || s[ind] == 'E') {
                if (ind == n - 1) {
                    return false;
                }
                else if (s[ind - 1] < '0' || s[ind - 1] > '9') {
                    return false;
                }
                e = true;
            } //check num in index before
            else if (s[ind] == '.' && visited.contains(s[ind]) == false) {
                if (e == true) {
                    return false;
                }
                if (ind == n-1) {
                    return true;
                }
            }
            else if (s[ind] < '0' || s[ind] > '9') {
                return false;
            }
            ind++;
        }
        return true;*/
        // note that if decimal point after e, false and only one e
        int n = s.length();
        bool isDot = false;
        bool nums = false;
        bool isE = false;
        for (int i = 0; i < n; i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                nums = true;
            }
            else if (s[i] == '+' || s[i] == '-') {
                if (i > 0 && (s[i - 1] != 'e' && s[i-1] != 'E')) {
                    return false;
                }
            }
            else if (s[i] == 'e' || s[i] == 'E') {
                if (isE || nums == false) {
                    return false;
                }
                isE = true;
                nums = false;
            }
            else if (s[i] == '.') {
                if (isDot || isE) {
                    return false;
                }
                isDot = true;
            }
            else {
                return false;
            }
        }
        return nums;
    }
};