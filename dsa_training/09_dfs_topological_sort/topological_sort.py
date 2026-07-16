class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
            
        # 0: Unvisited, 1: Visiting, 2: Visited/Safe
        state = {i: 0 for i in range(numCourses)}
        
        def dfs(node):
            if state[node] == 1:
                return False # Cycle
            if state[node] == 2:
                return True # Already validated
                
            state[node] = 1 # Mark as visiting
            for pre in graph[node]:
                if not dfs(pre):
                    return False
                    
            state[node] = 2 # Mark as safe
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
