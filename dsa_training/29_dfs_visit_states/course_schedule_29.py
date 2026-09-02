from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        TODO: Return true if you can finish all courses, else false.
        Implement cycle detection in a directed graph using DFS.
        You must track 3 states for each node:
        0 = unvisited
        1 = visiting (in the current DFS path)
        2 = visited (fully processed)
        """
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)
            
        state = [0] * numCourses
        
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
            
        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
        return True
