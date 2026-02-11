class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
        for src in graph.keys():
            graph[src].sort(reverse = True)
        stack = []
        res = []
        stack.append('JFK')
        while len(stack) > 0:
            ele = stack[-1]
            if ele in graph and len(graph[ele]) > 0:
                stack.append(graph[ele].pop())
            else:
                res.append(stack.pop())
        return res[::-1]