long long countValidSubstrings(char* s) {
    int n = strlen(s);
    long long total_substrings = (long long)n * (n + 1) / 2;
    long long invalid_substrings = 0;
    long long last_a = -1;
    long long last_ab = -1;
    long long last_abc = -1;
    int right = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'c') {
            if(last_ab != -1) {
                last_abc = last_ab;
            }
        }
        if (s[i] == 'b') {
            if (last_a != -1) {
                last_ab = last_a;
            }
        }
        if (s[i] == 'a') {
            last_a = i;
        }
        if (last_abc != -1) {
            invalid_substrings += (last_abc + 1);
        }
    }
    return total_substrings - invalid_substrings;
}