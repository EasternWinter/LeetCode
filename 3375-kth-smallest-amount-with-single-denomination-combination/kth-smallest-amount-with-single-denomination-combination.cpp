class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        int m = (1 << n);
        sort(coins.begin(), coins.end());
        vector<int> bit_count(m);
        vector<long long> lcm(m);
        long long l = k, r = 1ll * coins[0] * k + 1;

        for (int mask = 1; mask < m; mask++) {
            long long cur_lcm = 1;
            for (int i = 0; i < n; i++) {
                if (mask >> i & 1) {
                    long long tmp = cur_lcm / gcd(cur_lcm, coins[i]);
                    if (tmp <= r / coins[i]) {
                        cur_lcm = tmp * coins[i];
                    } else {
                        cur_lcm = r + 1;
                        break;
                    }
                    bit_count[mask]++;
                }
            }
            lcm[mask] = cur_lcm;
        }

        auto get = [&](long long x) -> long long {
            long long count = 0;
            for (int mask = 1; mask < m; mask++) {
                if (lcm[mask] > x) {
                    continue;
                }
                if (bit_count[mask] & 1) {
                    count += x / lcm[mask];
                } else {
                    count -= x / lcm[mask];
                }
            }
            return count;
        };

        while (l < r) {
            long long x = (l + r) >> 1;
            if (get(x) >= k) {
                r = x;
            } else {
                l = x + 1;
            }
        }
        return l;
    }
};