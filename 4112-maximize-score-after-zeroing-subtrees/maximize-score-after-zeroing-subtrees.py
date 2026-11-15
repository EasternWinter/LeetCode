class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)
        children: list[list[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        def dfs(u: int) -> int:
            if not children[u]:
                return score[u]
            sum_children = 0
            min_child = float('inf')
            for v in children[u]:
                child_dp = dfs(v)
                sum_children += child_dp
                if child_dp < min_child:
                    min_child = child_dp
            base = score[u] + sum_children
            if op[u] == 0:
                return base - min(0, int(min_child))
            return base - int(min_child)
        return dfs(0)