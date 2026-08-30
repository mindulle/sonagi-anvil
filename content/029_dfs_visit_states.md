# Prompt
Return true if you can finish all courses, else false.
This is a cycle detection problem in a directed graph.

# Buggy Code
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        visited = [False] * numCourses
        
        def dfs(node):
            if visited[node]:
                return True
            visited[node] = True
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            visited[node] = False
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
```

# Solution
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # 0: unvisited, 1: visiting, 2: visited
        state = [0] * numCourses
        
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
            
        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True
```
