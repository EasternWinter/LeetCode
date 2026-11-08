class Solution {
public:
    long long minCost(int n, string colors, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        vector<int> parent(n, -1);
        vector<int> order;
        order.reserve(n);
        order.push_back(0);
        for (int i = 0; i < n; ++i) {
            int u = order[i];
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        vector<long long> sub(n, 1);
        vector<long long> dp0(n, 0);
        vector<long long> dp1(n, 0);
        vector<long long> best_in_sub(n, 0);
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            long long sum_dp0 = 0;
            long long sum_min01 = 0;
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    sub[u] += sub[v];
                    sum_dp0 += dp0[v];
                    sum_min01 += min(dp0[v], dp1[v]);
                }
            }
            long long cost_to_B = (colors[u] == 'R') ? sub[u] : 0;
            long long cost_to_R = (colors[u] == 'B') ? sub[u] : 0;
            dp0[u] = cost_to_B + sum_dp0;
            dp1[u] = cost_to_R + sum_min01;
            best_in_sub[u] = min(dp0[u], dp1[u]);
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    long long candidate = cost_to_B + (sum_dp0 - dp0[v]) + best_in_sub[v];
                    best_in_sub[u] = min(best_in_sub[u], candidate);
                }
            }
        }
        return best_in_sub[0];
    }
};