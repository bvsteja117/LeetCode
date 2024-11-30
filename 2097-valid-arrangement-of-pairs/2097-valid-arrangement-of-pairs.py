from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        start = -1
        for p in graph:
            if out_degree[p] - in_degree[p] == 1:
                start = p
                break
        
        if start == -1:
            start = pairs[0][0]
        
        path = []
        
        def dfs(current):
            while graph[current]:
                next_node = graph[current].pop()
                dfs(next_node)
            path.append(current)
        
        dfs(start)
        
        path.reverse()
        return [[path[i], path[i+1]] for i in range(len(path)-1)]