class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjMap = {i: [] for i in range(n + 1)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        visited = [False] * (n + 1)
        cycles = set()
        cycleStart = -1

        def dfs(node, prev):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True

            visited[node] = True
            for nei in adjMap[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycles.add(node) 
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)
        for n1, n2 in reversed(edges):
            if n1 in cycles and n2 in cycles:
                return [n1, n2]
        return []
        