class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        '''count = 0
        sides = set()
        for edge in edges:
            sides.add(set(edge))
        def possFrom(start):
            s = nums[start]
            end = start + 1
            st = start
            def leg():
                while set(start, end) in sides:
                    s += nums[end]
                    st = end
                    end = end + 1
            '''
        n = len(nums)
        #Build the adjacency list for the full graph
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        validSubsetCount = 0
        
        #Total number of subsets is 2^n. Skip the empty subset.
        for mask in range(1, 1 << n):
            subsetNodes = []
            valueSum = 0
            
            #Identify nodes in the current subset and calculate their sum
            for i in range(n):
                if (mask >> i) & 1:
                    subsetNodes.append(i)
                    valueSum += nums[i]
            
            #Condition 1: Sum of node values must be even
            if valueSum % 2 != 0:
                continue
                
            #Condition 2: Induced subgraph must be connected
            start = subsetNodes[0]
            visited = set([start])
            queue = deque([start])

            while queue:
                cur = queue.popleft()
                for neighbour in adj[cur]:
                    if ((mask >> neighbour) & 1) and (neighbour not in visited):
                        visited.add(neighbour)
                        queue.append(neighbour)
            if len(visited) == len(subsetNodes):
                validSubsetCount += 1
        
        return validSubsetCount