long long countValidSubstrings(char* s) {
    int n = strlen(s);
    long long total_substrings = (long long)n * (n + 1) / 2;
    long long invalid_substrings = 0;
    int right = 0;
    for (int left = 0; left < n; left++) {
        while (right + 2 < n) {
            if (s[right] == 'a' && s[right + 1] == 'b' && s[right + 2] == 'c') {
                break;
            }
            right++;
        }
        if (right + 2 < n && s[right] == 'a' && s[right + 1] == 'b' && s[right + 2] == 'c') {
            invalid_substrings += (n - (right + 2));
        }
        if (left == right) {
            right ++;
        }
    }
    return total_substrings - invalid_substrings;
}