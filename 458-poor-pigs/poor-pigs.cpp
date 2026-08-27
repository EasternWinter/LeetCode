class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int base = minutesToTest / minutesToDie +1;
        long n = 1;
        int ans = 0;

        while (n < buckets){
            n *= base;
            ans++;
        }
        return ans;
    }
};