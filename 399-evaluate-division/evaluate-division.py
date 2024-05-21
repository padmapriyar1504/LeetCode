from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]
        
        result = []
        for C, D in queries:
            if C in graph and D in graph[C]:
                result.append(graph[C][D])
            else:
                result.append(-1.0)
        
        return result