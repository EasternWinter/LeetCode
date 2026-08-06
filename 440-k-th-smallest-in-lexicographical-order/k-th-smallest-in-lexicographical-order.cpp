class Solution {
public:
    int findKthNumber(long n, long k) {
        auto getGap = [&n](long a, long b) {
            long gap = 0;
            while (a <= n) {
                gap += min(n + 1, b) - a;
                a *= 10;
                b *= 10;
            }
            return gap;
        };
        long curNum = 1;
        for (int i = 1; i < k;) {
            long gap = getGap(curNum, curNum + 1);
            if (i + gap <= k) {
                i += gap;
                curNum++;
            }
            else {
                i++;
                curNum *= 10;
            }
        }
        return curNum;
    }
};